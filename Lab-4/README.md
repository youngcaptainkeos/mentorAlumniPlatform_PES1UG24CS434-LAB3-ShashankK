# Lab 4: VibeCoding — Coin Collector

**Student Name:** Shashank K  
**SRN:** PES1UG24CS434  
**Course:** Software Engineering (SE) Lab  
**Section:** Section H  
**Assigned Repo:** [SETAPESU26/06_coin_collector](https://github.com/SETAPESU26/06_coin_collector)

---

## Deliverables Summary

| Deliverable | Location / File | Description |
| :--- | :--- | :--- |
| **Before Video** | [`videos/before_recording.webm`](./videos/before_recording.webm) | 10s gameplay video showing the infinite score bug on coin overlap |
| **After Video** | [`videos/after_recording.webm`](./videos/after_recording.webm) | 10s gameplay video showing all features and bug fixes working |
| **Updated Code** | [`code/coin-collector/`](./code/coin-collector/) | Complete working Pygame code with all 4 tasks implemented |
| **Chat / Prompt History** | [`chat_history/Lab_4_VibeCoding_Session_Report.pdf`](./chat_history/Lab_4_VibeCoding_Session_Report.pdf)<br>[`chat_history/Lab_4_VibeCoding_Session_Report.md`](./chat_history/Lab_4_VibeCoding_Session_Report.md) | Full interaction log with prompt iterations, solutions, and tests |

---

## Tasks Completed

1. **Task 1: Fix Coin Collection Bug**
   - Coins score exactly once upon touch and are immediately removed from the active screen.
   - Dynamic respawn keeps the play area active and balanced.
2. **Task 2: Multiple Coin Types**
   - **Bronze** (1 pt, copper `#CD7F32`)
   - **Silver** (3 pts, silver `#C0C0C0`)
   - **Gold** (5 pts, gold `#FFD700`)
3. **Task 3: Obstacles & Lives System**
   - Added autonomous red hazard blocks bouncing off walls.
   - 3-lives system with a 1.5-second cooldown and visual flicker upon taking damage.
4. **Task 4: Timed Round & Game Over / Restart Flow**
   - 30-second round countdown timer on HUD.
   - Game Over screen with final score when time expires or lives reach 0.
   - Press **`[R]`** to restart a fresh round; **`[ESC]`** to quit.

---

## How to Run the Updated Game

```bash
cd code/coin-collector
pip install -r requirements.txt
python main.py
```
**Controls:**
- **Arrow Keys:** Move player
- **R:** Restart round (when Game Over)
- **ESC:** Quit
