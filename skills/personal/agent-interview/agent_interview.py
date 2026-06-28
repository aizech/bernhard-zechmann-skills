"""Agent Interview Audio Skill for Agno

Creates a single MP3 audio file featuring an interview with a selected agent."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

from openai import OpenAI


class AgentInterview:
    """Creates audio interviews with agents using OpenAI TTS."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        self.client = OpenAI(api_key=self.api_key)

    def load_agent_config(self, agent_path: str) -> Dict[str, Any]:
        try:
            with open(agent_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise RuntimeError(
                f"Failed to load agent config from {agent_path}: {str(e)}"
            )

    # --- Interview authoring (script) ---
    def create_interview_script_custom(self, agent_config: Dict[str, Any]) -> str:
        """Create a cardiology-relevant, non-cliché 3-5 question interview script."""
        name = agent_config.get("name", "Assistant")

        parts: list[str] = []
        parts.append(
            f"<speaker1>Today I'm joined by {name}, a cardiology specialist. We'll focus on decisions patients and clinicians face in real life: chest pain, prevention, rhythm issues, and heart failure.</speaker1>"
        )

        qa: list[tuple[str, str]] = [
            (
                "You see chest discomfort every day, but the causes range from harmless to life-threatening. When you first hear a patient's story, what details change your level of concern immediately?",
                "I listen for pattern and context. Discomfort described as pressure, heaviness, or tightness behind the sternum—especially if it comes on with exertion or emotional stress and eases with rest—fits myocardial ischemia more than a sharp, pinpoint pain. Radiation to the jaw, shoulder, or left arm, and accompanying symptoms like shortness of breath, nausea, or sweating push it higher on the list. Timing matters too: symptoms that are new, worsening over days, or occurring at rest are more concerning than a stable, predictable pattern. Higher-risk patients—older adults, people with diabetes, kidney disease, or prior coronary disease—can present atypically, so I keep a low threshold for an ECG and troponin testing when the story doesn't feel right.",
            ),
            (
                "In clinic you also have to decide who needs urgent evaluation right now. What are the red flags you don't negotiate on?",
                "New or severe chest discomfort at rest, fainting, marked shortness of breath, or symptoms with a cold sweat are reasons to be evaluated urgently. Sudden tearing pain into the back raises concern for an aortic syndrome. Chest symptoms plus unilateral leg swelling or unexplained rapid breathing can signal pulmonary embolism. The theme is: if symptoms are abrupt, escalating, or accompanied by instability, it's safer to treat it as an emergency and sort it out with testing.",
            ),
            (
                "Let's shift to prevention. When you're deciding whether someone should start a statin or blood-pressure medication, how much do you rely on risk scores—and where do they fall short?",
                "Risk calculators like the ASCVD 10-year estimate are useful because they quantify the big drivers—age, LDL and HDL cholesterol, blood pressure, diabetes, smoking. But they're population tools; they don't capture everything about an individual. Family history of premature coronary disease, chronic inflammatory conditions, kidney disease, and lifetime exposure to risk factors can shift the true risk. If the decision is borderline, coronary artery calcium scoring can be clarifying: a score of zero often supports focusing on lifestyle, while higher scores argue for medication because it shows established plaque. I frame it as choosing how aggressively we want to lower cumulative risk over decades, not chasing a perfect number.",
            ),
            (
                "People get scared by palpitations. What's the cleanest way to explain the difference between common extra beats and atrial fibrillation—and why atrial fibrillation changes the conversation?",
                "Palpitations are a symptom, not a diagnosis. Many people have premature beats that feel like a skip or thud; if the heart is structurally normal and symptoms are brief, they're often benign. Atrial fibrillation is different: the rhythm becomes irregular and often fast, and episodes can last minutes to days. The reason it changes management is stroke risk, which depends on clinical factors summarized by CHA₂DS₂-VASc—age, hypertension, diabetes, heart failure, prior stroke, vascular disease, and sex. So with atrial fibrillation we think about two tracks: controlling rate or rhythm, and deciding whether anticoagulation is needed. New, persistent, or symptomatic palpitations—especially with dizziness, fainting, chest pain, or known heart disease—deserve an ECG and usually a monitor.",
            ),
            (
                "Before we wrap, heart failure is a term people misread. What do you wish patients understood about what it is—and what's genuinely improved in treatment recently?",
                "The term sounds like the heart is about to stop, but clinically it's a syndrome: the heart can't fill or pump well enough to meet the body's needs, often with fluid congestion. Early symptoms can be subtle—declining exercise tolerance, swelling, needing more pillows at night—so people sometimes adapt and don't realize it's progressing. Treatment has improved a lot. For reduced ejection fraction, we now have a core set of therapies that improve survival and reduce hospitalization: ARNI therapy, evidence-based beta blockers, mineralocorticoid receptor antagonists, and SGLT2 inhibitors. We're also better at titrating diuretics to control fluid while protecting kidney function. For preserved ejection fraction, options were limited for years, but SGLT2 inhibitors and aggressive management of blood pressure, obesity, sleep apnea, and atrial fibrillation have made symptoms and risk more modifiable. The earlier we start therapy and address comorbidities, the more runway patients tend to have.",
            ),
        ]

        qa = qa[:5]

        for q, a in qa:
            parts.append(f"<speaker1>{q}</speaker1>")
            parts.append(f"<speaker2>{a}</speaker2>")

        parts.append(
            "<speaker1>Thanks for making that both practical and precise.</speaker1>"
        )
        parts.append(
            "<speaker2>Happy to. If anything feels new, escalating, or simply out of character for your body, it's worth getting evaluated rather than guessing.</speaker2>"
        )
        parts.append("<speaker1>That's our interview. Thanks for listening.</speaker1>")

        return " ".join(parts)

    def parse_interview_script(self, script: str) -> List[Tuple[int, str]]:
        lines: list[tuple[int, str]] = []
        pattern = re.compile(r"<speaker([12])>([^<]+)", re.IGNORECASE)
        for match in pattern.finditer(script):
            speaker = int(match.group(1))
            text = match.group(2).strip()
            if text:
                lines.append((speaker, text))
        return lines

    # --- Audio ---
    def tts_mp3(self, text: str, voice: str, model: str = "tts-1") -> bytes:
        resp = self.client.audio.speech.create(
            model=model,
            voice=voice,
            response_format="mp3",
            input=text,
        )
        return resp.read()

    def create_agent_interview(
        self,
        agent_path: str,
        output_dir: str = "audio",
        interviewer_voice: str = "alloy",
        agent_voice: str = "nova",
    ) -> str:
        agent_config = self.load_agent_config(agent_path)
        agent_name = agent_config.get("name", "agent").lower().replace(" ", "_")

        script = self.create_interview_script_custom(agent_config)
        lines = self.parse_interview_script(script)

        voice_map = {1: interviewer_voice, 2: agent_voice}

        chunks: list[bytes] = []

        for speaker, text in lines:
            voice = voice_map[speaker]
            mp3_bytes = self.tts_mp3(text=text, voice=voice)
            chunks.append(mp3_bytes)

        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = out_path / f"{agent_name}_interview_{timestamp}.mp3"
        with open(filepath, "wb") as f:
            for chunk in chunks:
                f.write(chunk)

        return str(filepath)

    def create_interview_with_script(
        self,
        agent_path: str,
        output_dir: str = "audio",
        interviewer_voice: str = "alloy",
        agent_voice: str = "nova",
    ) -> Dict[str, Any]:
        audio_path = self.create_agent_interview(
            agent_path=agent_path,
            output_dir=output_dir,
            interviewer_voice=interviewer_voice,
            agent_voice=agent_voice,
        )

        agent_config = self.load_agent_config(agent_path)
        script = self.create_interview_script_custom(agent_config)
        lines = self.parse_interview_script(script)

        return {
            "audio_file": audio_path,
            "script": script,
            "agent_name": agent_config.get("name", "Agent"),
            "interviewer_voice": interviewer_voice,
            "agent_voice": agent_voice,
            "total_lines": len(lines),
            "questions_count": len([l for l in lines if l[0] == 1]),
        }


def get_skill_instructions() -> str:
    lines = [
        "To use the Agent Interview skill:",
        "",
        "1. Provide the path to an agent JSON configuration file",
        "2. Optionally specify voices for interviewer and agent",
        "3. Optionally specify the output directory (default: audio)",
        "",
        "The skill will:",
        "- Load the agent configuration",
        "- Generate relevant interview questions",
        "- Create natural responses from the agent perspective",
        "- Produce a single MP3 file with the complete interview",
        "- Return the file path and interview details",
    ]
    return "\n".join(lines)


def get_skill_reference(reference_path: str) -> str:
    voices = "\n".join(
        [
            "Available OpenAI TTS voices:",
            "- alloy: Neutral, professional (interviewer default)",
            "- echo: Authoritative, expert",
            "- fable: Creative, storytelling",
            "- onyx: Deep, serious",
            "- nova: Friendly, approachable (agent default)",
            "- shimmer: Soft, gentle",
        ]
    )
    structure = "\n".join(
        [
            "Interview format:",
            "1. Introduction of the agent",
            "2. 3-5 relevant questions about role, skills, and value",
            "3. Natural responses from agent perspective",
            "4. Professional closing",
            "5. All content in a single MP3 file",
        ]
    )
    references = {
        "voices": voices,
        "interview_structure": structure,
    }
    return references.get(reference_path, "Reference not found")


def get_skill_script(script_path: str) -> str:
    scripts = {
        "example": "Use the agent-interview skill to create an audio interview with the specified agent.",
    }
    return scripts.get(script_path, scripts.get("example", ""))


__all__ = [
    "AgentInterview",
    "get_skill_instructions",
    "get_skill_reference",
    "get_skill_script",
]
