---
name: scratch-coder
description: Create Scratch 3.0 projects using Python and ScratchGen. Use when the user wants to generate a .sb3 file with sprites, scripts, and assets.
license: MIT
compatibility: claude-code opencode github-copilot devin pi cursor
---

# Scratch Coder

Create Scratch 3.0 projects with Python and ScratchGen.

## Setup

```bash
pip install "ScratchGen~=1.1"
```

## Quick start

```python
from ScratchGen import *

project = Project()
sprite = project.createSprite('Cat')

sprite.createScript(
    WhenFlagClicked(),
    Show(),
    Say('Hello!')
)

project.save('hello.sb3')
```

## Common pitfalls

- Sprites are hidden by default. Call `Show()` in `WhenFlagClicked()`.
- Sprites have no default costume. Add costumes via `addCostume()` or inject them after saving.
- `Broadcast()` / `WhenBroadcastReceived()` use null IDs in ScratchGen. Use `ChangeVariable` on global stage variables for cross-sprite state instead.
- `GetAttribute` requires ScratchGen constants, not strings: `GetAttribute(Y_POSITION, ball)`.
- `Stop(ALL)` clears speech bubbles before rendering. Use a `game_over` state variable plus a dedicated message sprite.
- Stage fence clamps sprites at `y = -180` to `180`. Keep detection thresholds inside the bounds.

## Stage coordinates

- x: -240 to 240
- y: -180 to 180

## Physics tips

- Keep `MoveSteps(N)` <= half the target sprite's width to avoid tunneling.
- For axis-aligned games, store direction as `dx`/`dy` stage variables and move with `ChangeX(Multiply(dx, speed))`.

## Save pipeline

```
project.save() -> add_costumes() -> add_monitors()
```

## Testing

```bash
python -c "import zipfile; print(zipfile.ZipFile('project.sb3').namelist())"
```

Open the file in TurboWarp to verify.

## Reference

- `references/block-reference.md` — complete block reference
