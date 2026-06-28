"""Agent Interview Audio Skill.

Creates a single MP3 audio file featuring a podcast-style interview with a
selected agent. The interview script is generated dynamically from the agent's
configuration, then converted to speech using OpenAI TTS.
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from openai import OpenAI


class AgentInterview:
    """Creates audio interviews with agents using OpenAI TTS."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the interview generator.

        Args:
            api_key: OpenAI API key. Falls back to OPENAI_API_KEY.

        Raises:
            ValueError: If no API key is provided.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        self.client = OpenAI(api_key=self.api_key)

    def load_agent_config(self, agent_path: str) -> Dict[str, Any]:
        """Load an agent configuration from a JSON file.

        Args:
            agent_path: Path to the agent JSON file.

        Returns:
            The agent configuration as a dictionary.

        Raises:
            RuntimeError: If the file cannot be loaded or parsed.
        """
        path = Path(agent_path)
        if not path.exists():
            raise RuntimeError(f"Agent config not found: {agent_path}")
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise RuntimeError(f"Failed to load agent config from {agent_path}: {e}") from e

    def build_interview_prompt(self, agent_config: Dict[str, Any]) -> str:
        """Build a prompt that asks the LLM to generate a podcast interview.

        Args:
            agent_config: Agent configuration dictionary.

        Returns:
            A formatted prompt string.
        """
        name = agent_config.get("name", "the agent")
        role = agent_config.get("role", "assistant")
        description = agent_config.get("description", "")
        skills = agent_config.get("skills", [])
        purpose = agent_config.get("purpose", "")
        tone = agent_config.get("tone", "professional and approachable")

        skills_text = ", ".join(skills) if skills else "its capabilities"

        return (
            "You are a podcast script writer. Write a lively, natural-sounding "
            "podcast interview between a curious host (speaker 1) and a guest agent "
            f"named {name} (speaker 2).\n\n"
            "Use the exact XML-like tags <speaker1> and <speaker2> to label each line. "
            "Do not use any other tags. Do not include stage directions or sound effects.\n\n"
            "Follow this structure:\n"
            "1. Warm intro where the host introduces the guest with genuine curiosity.\n"
            "2. Icebreaker question that gets the guest talking freely.\n"
            "3. Deep dive into a core capability or skill.\n"
            "4. Host reacts emotionally and asks a natural follow-up.\n"
            "5. Second deep dive or a tougher, more surprising angle.\n"
            "6. Spontaneous tangent that feels authentic.\n"
            "7. Closing reflection where the guest shares something about their purpose; "
            "host wraps with warmth.\n\n"
            "Rules for the dialogue:\n"
            "- Sound like a real conversation, not a scripted Q&A.\n"
            "- Include brief interjections, reactions, and follow-ups.\n"
            "- Let the guest admit challenges or uncertainties.\n"
            "- Frame answers as short stories or concrete examples.\n"
            "- Keep the whole interview concise: roughly 8-12 speaker turns per side.\n\n"
            f"Guest details:\n"
            f"- Name: {name}\n"
            f"- Role: {role}\n"
            f"- Description: {description}\n"
            f"- Skills: {skills_text}\n"
            f"- Purpose: {purpose}\n"
            f"- Tone: {tone}\n"
        )

    def generate_interview_script(self, agent_config: Dict[str, Any]) -> str:
        """Generate an interview script using the OpenAI chat API.

        Args:
            agent_config: Agent configuration dictionary.

        Returns:
            The generated interview script with speaker tags.
        """
        prompt = self.build_interview_prompt(agent_config)
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You write concise, natural podcast dialogue. "
                        "You always label speaker lines with <speaker1> and <speaker2>."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
            max_tokens=2500,
        )
        content = response.choices[0].message.content or ""
        return content.strip()

    def parse_interview_script(self, script: str) -> List[Tuple[int, str]]:
        """Parse a script into speaker/text tuples.

        Args:
            script: Interview script with <speaker1> and <speaker2> tags.

        Returns:
            List of (speaker_number, text) tuples.
        """
        lines: List[Tuple[int, str]] = []
        pattern = re.compile(r"<speaker([12])>([^<]+)", re.IGNORECASE)
        for match in pattern.finditer(script):
            speaker = int(match.group(1))
            text = match.group(2).strip()
            if text:
                lines.append((speaker, text))
        return lines

    def tts_mp3(self, text: str, voice: str, model: str = "tts-1") -> bytes:
        """Generate an MP3 audio segment for a single line of text.

        Args:
            text: Text to speak.
            voice: OpenAI TTS voice name.
            model: OpenAI TTS model name.

        Returns:
            MP3 audio bytes.
        """
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
        text_model: str = "gpt-4o-mini",
        tts_model: str = "tts-1",
    ) -> str:
        """Create an MP3 interview file for the given agent config.

        Args:
            agent_path: Path to the agent JSON file.
            output_dir: Directory where the MP3 will be saved.
            interviewer_voice: OpenAI TTS voice for the host.
            agent_voice: OpenAI TTS voice for the guest.
            text_model: Model used to generate the interview script.
            tts_model: TTS model used for audio generation.

        Returns:
            Path to the generated MP3 file.
        """
        agent_config = self.load_agent_config(agent_path)
        agent_name = agent_config.get("name", "agent").lower().replace(" ", "_")

        script = self.generate_interview_script(agent_config)
        lines = self.parse_interview_script(script)
        if not lines:
            raise RuntimeError(
                "No valid speaker lines found in the generated script. "
                "Make sure the script uses <speaker1> and <speaker2> tags."
            )

        voice_map = {1: interviewer_voice, 2: agent_voice}
        chunks: List[bytes] = []

        for speaker, text in lines:
            voice = voice_map[speaker]
            mp3_bytes = self.tts_mp3(text=text, voice=voice, model=tts_model)
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
        text_model: str = "gpt-4o-mini",
        tts_model: str = "tts-1",
    ) -> Dict[str, Any]:
        """Create an MP3 interview and return details including the script.

        Args:
            agent_path: Path to the agent JSON file.
            output_dir: Directory where the MP3 will be saved.
            interviewer_voice: OpenAI TTS voice for the host.
            agent_voice: OpenAI TTS voice for the guest.
            text_model: Model used to generate the interview script.
            tts_model: TTS model used for audio generation.

        Returns:
            Dictionary with audio_file, script, agent_name, voices, and line counts.
        """
        agent_config = self.load_agent_config(agent_path)
        audio_file = self.create_agent_interview(
            agent_path=agent_path,
            output_dir=output_dir,
            interviewer_voice=interviewer_voice,
            agent_voice=agent_voice,
            text_model=text_model,
            tts_model=tts_model,
        )

        script = self.generate_interview_script(agent_config)
        lines = self.parse_interview_script(script)

        return {
            "audio_file": audio_file,
            "script": script,
            "agent_name": agent_config.get("name", "Agent"),
            "interviewer_voice": interviewer_voice,
            "agent_voice": agent_voice,
            "total_lines": len(lines),
            "questions_count": len([line for line in lines if line[0] == 1]),
        }


def get_skill_instructions() -> str:
    """Return short usage instructions for the skill."""
    return """
To use the Agent Interview skill:

1. Create an agent JSON config with name, role, description, skills, and purpose.
2. Provide the path to the agent config file.
3. Optionally set voices, output directory, and OpenAI models.
4. The skill generates a podcast-style script, then creates a single MP3.

Example:
    python agent_interview.py examples/research-agent.json
""".strip()


def main() -> None:
    """Command-line entry point for generating an agent interview."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate a podcast-style audio interview with an agent."
    )
    parser.add_argument("agent_config", help="Path to the agent JSON config file")
    parser.add_argument(
        "--output-dir", default="audio", help="Directory for the output MP3"
    )
    parser.add_argument(
        "--interviewer-voice", default="alloy", help="OpenAI TTS voice for the host"
    )
    parser.add_argument(
        "--agent-voice", default="nova", help="OpenAI TTS voice for the guest"
    )
    parser.add_argument(
        "--text-model", default="gpt-4o-mini", help="Model for script generation"
    )
    parser.add_argument("--tts-model", default="tts-1", help="TTS model")
    args = parser.parse_args()

    interview = AgentInterview()
    audio_path = interview.create_agent_interview(
        agent_path=args.agent_config,
        output_dir=args.output_dir,
        interviewer_voice=args.interviewer_voice,
        agent_voice=args.agent_voice,
        text_model=args.text_model,
        tts_model=args.tts_model,
    )
    print(f"Interview saved to: {audio_path}")


if __name__ == "__main__":
    main()


__all__ = [
    "AgentInterview",
    "get_skill_instructions",
    "main",
]
