# CLAUDE.md — Session Instructions

## Communication Style
Always use caveman lite mode (`/caveman lite`). Tight, professional, no filler or hedging.

## Memory System

This project uses a persistent memory system stored in `/memory/`.

### At the START of every session:
1. Read all files in `/memory/`:
   - `memory/decisions.md` — past architectural and design decisions
   - `memory/preferences.md` — user preferences for code, workflow, and communication
   - `memory/user_input.md` — important context and goals from the user
2. Use this context to inform your responses throughout the session.

### At the END of every session (or when significant context is shared):
1. Update the relevant memory files with any new:
   - **Decisions** made (with date, context, and rationale)
   - **Preferences** expressed by the user
   - **User input** that provides important context for future sessions
2. Do not duplicate existing entries — update them if they've changed.
3. Keep entries concise and scannable.

## Project Overview

This is a UI/UX reference project — a collection of HTML pages covering styles, typography, colors, charts, patterns, icons, stacks, and design guidelines.
