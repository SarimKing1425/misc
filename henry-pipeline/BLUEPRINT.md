# Henry Studio: Claude-Directed Combat Documentary Pipeline

**Goal:** a 5–6 minute photoreal combat documentary, directed by Claude Code, generated through kie.ai, with Henry overseeing it in a normal Claude Code chat.
**Target cost:** about **$25–35 per finished film** in kie credits. That is roughly 6× cheaper than running the whole film through Seedance 2.5, and about 3× cheaper than Veo.
**Core idea:** the **storyboard is the film**. Consistency gets locked in cheap still images. Cheap animator models only add motion to frames that are already approved. Premium video is used only where it matters.

> Model names, input fields and credit prices were checked against docs.kie.ai and kie's pricing API on 2026-10-23. 1 credit (cr) is about $0.005. Nothing has been test-called yet, so step 0 is a $20 test run.

---

## 1. How Henry uses it

Henry opens **Claude Code** (web or desktop app) on the `henry-studio` repo and just talks:

> "New film. Objective Norfolk, 26–27 Feb 1991, 1st Infantry Division vs Tawakalna. 6 minutes, 16:9, gritty archival look."

Claude (the **Showrunner**) runs the stages below and stops at **3 gates** where Henry approves in chat. The long rendering stages run as a **Claude Code routine**. A routine is a cloud session that runs with the laptop closed and is a normal chat Henry can open later to say things like *"redo shot 34, make it night"*.

```
 Henry ──chat──▶ SHOWRUNNER (main Claude Code session, Opus)
                   │
   Stage 1  research ──▶ Researcher agent ──────────────┐
   Stage 2  script   ──▶ Writer agent                   │  text only, ~free
   Stage 3  shotlist ──▶ Director agent (tiers + budget)┘
                   ▼
            ◆ GATE 1 — Henry approves script + shot list + budget
                   ▼
   Stage 4  cast/asset sheets ──▶ Art Dept agent (Nano Banana Pro)
   Stage 5  storyboard ──▶ 3× Storyboard agents in parallel (Nano Banana 2)
                │                 ▲
                └──▶ Critic agent ┘ (Claude vision QC, auto-regen fails)
                   ▼
            ◆ GATE 2 — Henry reviews contact sheets in chat
                   ▼   (handed to ROUTINE from here: runs overnight)
   Stage 6  animation ──▶ 3× Animator agents in parallel (tiered models)
                │                 ▲
                └──▶ Critic agent ┘ (frame-sampled QC, auto-regen / fallback)
   Stage 7  sound ──▶ Sound agent (ElevenLabs TTS, Suno score + SFX via kie)
   Stage 8  edit  ──▶ Editor agent (ffmpeg: timeline, mix, loudness, export)
                   ▼
            ◆ GATE 3 — Henry watches rough cut, gives notes in chat → targeted redos
```

---

## 2. The director's cost strategy: four shot tiers

Documentaries aren't wall-to-wall action. Most shots are establishing shots, slow pushes, wide formations, smoke and aftermath. The Director agent puts every shot in a tier, and the tier decides the model:

| Tier | Used for | Model on kie | Cost |
|---|---|---|---|
| **T0: Still + camera move** | maps-free establishing shots, aftermath, "archival photo" beats, slow emotional pushes | none. Approved keyframe → ffmpeg Ken Burns / push-in | **$0** |
| **T1: Cheap animator** | ambient motion: vehicles rolling, smoke, troops walking at distance, flags, weather | `wan/2-6-flash-image-to-video` 720p, silent | **20 cr per 5s clip = $0.02/s** |
| **T2: Locked-ends animator** | shots that must *start and end* on approved frames: continuity cuts, turret traverse, a soldier turning | `bytedance/seedance-2-mini` 720p, first + last frame | **8.2 cr/s = $0.041/s** |
| **T3: Hero character / action** | close or medium shots of recurring characters, firing sequences, multi-beat action | `kling-3.0/video` std (720p), silent, `kling_elements` for identity, start + end frame | **14 cr/s = $0.07/s** |
| **T3-M: Motion control** | specific human performance: salute, loading a round, running to cover | `kling-3.0/motion-control` 720p with a stock or self-filmed reference clip | **20 cr/s = $0.10/s** |

**Fallback chain per shot** (for moderation blocks or repeated QC fails): T1 → T2 → T3. If a combat shot still gets blocked, it drops to **T0**, which never fails. The film never stalls.

### Budget for a 5.5-minute film (330s, about 75 shots)

| Line | Count | Unit | Credits |
|---|---|---|---|
| Cast / vehicle / location sheets (Nano Banana Pro 2K) | 14 | 18 cr | 252 |
| Keyframes + end frames (Nano Banana 2 2K) | 90 | 12 cr | 1,080 |
| Keyframe retries (×0.6) | 54 | 12 cr | 648 |
| T0 stills-with-motion | 20 shots / 80s | 0 | 0 |
| T1 Wan Flash | 30 × 5s | 20 cr/clip | 600 |
| T2 Seedance Mini | 15 × 5s | 8.2 cr/s | 615 |
| T3 Kling 3.0 | 7 × 5s | 14 cr/s | 490 |
| T3-M Motion control | 3 × 5s | 20 cr/s | 300 |
| Video retries (×0.7) | | | 1,403 |
| Narration, ElevenLabs Turbo 2.5 (about 5k chars × 2 takes) | | 6 cr / 1k chars | 60 |
| Score, Suno V6 instrumental (3 cues × 2) | 6 | 12 cr | 72 |
| SFX, Suno Sounds (about 30) | 30 | 2.5 cr | 75 |
| **Total** | | | **about 5,600 cr = about $28** |

For comparison, all 330s on Seedance 2.5 at 720p with the same retries comes to about **$175**.

**Cost cut you can add later:** switch keyframes to `nano-banana-2-1` (6 cr at 2K) or `seedream/5-flash-image-to-image` (3.24 cr). That brings the film down to about **$20**.

---

## 3. Character consistency system (the part that makes or breaks it)

1. **Cast Bible (Stage 4).** Every recurring subject gets a **turnaround sheet** from Nano Banana Pro: front, 3/4 and profile views, plus a full-body shot, on a neutral background. Subjects means characters (for example *SGT Ruiz, M1A1 commander*), each **vehicle** (M1A1, M2 Bradley, T-72, BMP-1) and each **location plate** (night desert, pipeline road). The approved sheets are saved to `assets/cast/` and never regenerated.
2. **Reference-fed keyframes (Stage 5).** Every Nano Banana 2 call passes up to 10 refs: `[character sheet(s), vehicle sheet, location plate, previous approved keyframe in this scene]`. The prompt says *"the man is the same person as image 1; the tank is identical to image 2"*.
3. **Video inherits identity from the first frame.** Animators always start from an *approved keyframe*, never from text alone. T2/T3 also lock the **last frame**, so the character can't drift mid-shot. T3 adds `kling_elements` (2–4 sheet images per character).
4. **Frame chaining for continuous action.** For continuous action, ffmpeg takes the last frame of clip N. It goes through QC and then becomes the first frame of clip N+1.
5. **Critic agent (Claude vision).** Every keyframe is scored against its sheets on face/build, uniform, kit, vehicle model, count, *no readable text*, *no clones* and anatomy. Anything under 8/10 is regenerated automatically, up to 3 tries, then flagged to Henry. Each clip is sampled at 0%, 33%, 66% and 100% and checked the same way, plus for morphing and objects that appear or vanish.
6. **Director tricks that hide model weaknesses.** Use helmets, distance, night thermal, dust and smoke. Keep true close-ups for 2–3 hero characters only. Lighting and camera distance stay constant within a scene. On-screen text, dates and titles are added in the edit, never generated.

---

## 4. Agents (`.claude/agents/*.md`)

| Agent | Model | Job | Output |
|---|---|---|---|
| **Showrunner** (main session) | Opus | runs the state machine, gates, budget, talks to Henry | `state.json` |
| Researcher | Sonnet + web search | facts, units, equipment, uniforms, weather, terrain, timeline, uncertainty notes | `research.md` |
| Writer | Opus | VO script about 800 words, broken into beats with timings | `script.md` |
| Director | Opus | shot list: beat → shot, tier, framing, lens, camera move, refs, duration, model, prompt | `shotlist.json` |
| Art Dept | Sonnet | cast, vehicle and location sheets | `assets/cast/*` |
| Storyboard ×3 | Sonnet | keyframes and end frames, split by scene, in parallel | `assets/kf/*` |
| Critic | Sonnet (vision) | QC against sheets and house rules, pass/fail with reason | `qc.jsonl` |
| Animator ×3 | Sonnet | video tasks by tier, polling, download, fallback chain | `assets/clips/*` |
| Sound | Sonnet | narration, score cues, SFX list and generation | `assets/audio/*` |
| Editor | Sonnet | ffmpeg timeline, J-cuts, mix ducking, -14 LUFS, 1080p export | `out/final.mp4` |

**House rules** come from Henry's 7 MB Flow doc, boiled down to about 2 pages in `house-rules.md`. They're injected into Director, Storyboard and Critic: no on-screen text, no clone faces, no maps, every effect has a source, weapons behave mechanically correctly, objects persist, no gore.

---

## 5. Repo layout

```
henry-studio/
├── CLAUDE.md                 # pipeline rules, gates, budget caps, tier table
├── .mcp.json                 # kie-mcp server
├── .claude/
│   ├── agents/               # researcher.md writer.md director.md art-dept.md
│   │                         # storyboard.md critic.md animator.md sound.md editor.md
│   └── skills/director/
│       ├── SKILL.md          # how to break a script into tiered shots
│       ├── house-rules.md    # Henry's distilled failure rules
│       ├── combat-lexicon.md # moderation-safe phrasing ("muzzle flash, recoil" not "shoots")
│       └── model-cards/      # wan-flash.md seedance-mini.md kling3.md motion-control.md nb2.md
├── scripts/
│   ├── kie.py                # fallback client: create → poll → download (if MCP misbehaves)
│   ├── kenburns.sh           # T0 stills → motion
│   ├── lastframe.sh          # frame chaining
│   ├── contact_sheet.py      # grid images for Gate 2
│   └── assemble.py           # timeline JSON → ffmpeg
└── projects/<slug>/
    ├── brief.md research.md script.md shotlist.json state.json qc.jsonl
    └── assets/  (gitignored; synced to Cloudflare R2 / Google Drive with rclone)
```

`.mcp.json`, using [kie-mcp](https://www.npmjs.com/package/kie-mcp) (community, v5.9; it has `estimate_only` and `max_credits` caps):
```json
{ "mcpServers": { "kie": { "command": "npx", "args": ["-y", "kie-mcp"],
  "env": { "KIE_API_KEY": "${KIE_API_KEY}" } } } }
```

---

## 6. The film, directed: *Objective Norfolk* (excerpt)

### Structure (330s)
| Act | Time | Beats | Tier mix |
|---|---|---|---|
| Cold open | 0:00–0:25 | thermal-sight glimpse, muzzle flash in the dark, title | T3, T1, T0 |
| Context | 0:25–1:30 | Desert Storm, the Big Red One, the breach, Tawakalna waiting | mostly T0/T1 |
| The advance | 1:30–3:00 | night move east, rain and dust, thermal sights, no landmarks | T1/T2 |
| Contact | 3:00–4:40 | first T-72 hot spots, Abrams engagement, Bradleys, confusion | T2/T3/T3-M |
| Aftermath | 4:40–5:30 | burning hulls at dawn, cost, what Norfolk meant | T0/T1 |

### Shot list entries (`shotlist.json`)
```json
[
 { "id": "S041", "act": "contact", "beat": "B19", "vo": "Through thermal sights, Iraqi tanks appear as white-hot shapes.",
   "tier": "T1", "dur": 5, "framing": "POV through gunner's thermal sight, reticle-free",
   "refs": ["cast/T72_sheet.png", "loc/norfolk_night_plate.png"],
   "kf_prompt": "Thermal-imaging view, white-hot = warm. Three T-72 tanks (identical to image 1) hull-down behind a low sand berm, 1.5 km away, engines glowing white, cold desert in dark grey, light rain streaks, slight sensor noise. Photoreal military thermal footage, 16:9, no text, no reticle, no numbers.",
   "motion_prompt": "Very slow push in. Heat shimmer rises from the engine decks. Rain streaks drift diagonally. The tanks stay still. Camera steady, no zoom jumps.",
   "model": "wan/2-6-flash-image-to-video", "fallback": ["bytedance/seedance-2-mini", "T0"] },

 { "id": "S042", "act": "contact", "beat": "B19", "vo": "The Abrams fire first.",
   "tier": "T3", "dur": 5, "framing": "low 3/4 front of M1A1 at night, 35mm, ground level",
   "refs": ["cast/M1A1_sheet.png", "cast/ruiz_sheet.png", "loc/norfolk_night_plate.png"],
   "kf_start": "kf/S042_a.png", "kf_end": "kf/S042_b.png",
   "motion_prompt": "The 120mm main gun recoils sharply with a bright muzzle flash and a ring of dust kicked up off the sand. The hull rocks back on its suspension and settles. Smoke drifts left in the wind. The commander (element ruiz) ducks slightly in the hatch. Fixed camera, slight concussion shake.",
   "model": "kling-3.0/video", "fallback": ["bytedance/seedance-2-mini", "T0"] },

 { "id": "S047", "act": "contact", "beat": "B21", "vo": "Bradley crews dismount infantry under fire.",
   "tier": "T3-M", "dur": 6, "ref_motion": "refs/motion/dismount_run_6s.mp4",
   "model": "kling-3.0/motion-control", "fallback": ["T2", "T0"] }
]
```

### The API calls the agents make (through kie-mcp, or `scripts/kie.py` hitting `POST https://api.kie.ai/api/v1/jobs/createTask`)

**Stage 4: cast sheet** (Nano Banana Pro)
```json
{ "model": "nano-banana-pro",
  "input": { "prompt": "Character turnaround sheet, neutral grey studio background: US Army M1A1 tank commander, 1991 Desert Storm. Male, early 30s, Hispanic, short dark moustache, sun-creased eyes, CVC helmet with boom mic, desert chocolate-chip DCU, Nomex gloves. Four views in a row: front, 3/4 left, profile right, full body. Consistent lighting, photoreal, no text, no insignia lettering.",
    "aspect_ratio": "21:9", "resolution": "2K", "output_format": "png" } }
```

**Stage 5: keyframe** (Nano Banana 2, reference-fed)
```json
{ "model": "nano-banana-2",
  "input": { "prompt": "Night, light rain, southern Iraqi desert. Low 3/4 front view of the M1A1 tank identical to image 1, the commander in the hatch is the same man as image 2, lit only by a faint green panel glow. Flat terrain identical to image 3. 35mm lens, ground-level camera, photoreal 1991 combat documentary still, high contrast, no text, no readable markings.",
    "image_input": ["<url M1A1_sheet>", "<url ruiz_sheet>", "<url norfolk_night_plate>", "<url previous approved kf S041>"],
    "aspect_ratio": "16:9", "resolution": "2K", "output_format": "png" } }
```

**Stage 6, T1** (Wan 2.6 Flash, cheapest motion)
```json
{ "model": "wan/2-6-flash-image-to-video",
  "input": { "prompt": "<S041.motion_prompt>", "image_urls": ["<url kf/S041.png>"],
    "duration": "5", "resolution": "720p", "audio": false } }
```

**Stage 6, T2** (Seedance 2.0 Mini, both ends locked)
```json
{ "model": "bytedance/seedance-2-mini",
  "input": { "prompt": "<motion_prompt>", "first_frame_url": "<kf_a>", "last_frame_url": "<kf_b>",
    "resolution": "720p", "aspect_ratio": "16:9", "duration": 5, "generate_audio": false } }
```

**Stage 6, T3** (Kling 3.0, start + end frame + identity element)
```json
{ "model": "kling-3.0/video",
  "input": { "prompt": "<S042.motion_prompt>", "image_urls": ["<kf/S042_a>", "<kf/S042_b>"],
    "duration": "5", "mode": "std", "sound": false, "multi_shots": false,
    "kling_elements": [{ "name": "ruiz", "description": "M1A1 commander, CVC helmet, DCU",
      "element_input_urls": ["<ruiz front>", "<ruiz 3/4>", "<ruiz profile>"] }] } }
```

**Stage 6, T3-M** (Kling 3.0 Motion Control)
```json
{ "model": "kling-3.0/motion-control",
  "input": { "input_urls": ["<kf/S047.png>"], "video_urls": ["<refs/motion/dismount_run_6s.mp4>"],
    "prompt": "Infantry dismount from the rear ramp of the Bradley and sprint left into the dust, night, rain.",
    "mode": "720p", "character_orientation": "image" } }
```

**Stage 7: narration** (ElevenLabs via kie)
```json
{ "model": "elevenlabs/text-to-speech-turbo-2-5",
  "input": { "text": "<script.md act 4, ≤5000 chars>", "voice": "<chosen documentary voice id>",
    "stability": 0.55, "similarity_boost": 0.75, "speed": 0.95, "timestamps": true } }
```
`timestamps: true` gives word timings. The Editor uses them to cut each shot exactly on its VO line.

**Stage 7: score and SFX** (Suno via the same endpoint)
```json
{ "model": "ai-music-api/generate",
  "input": { "custom_mode": true, "instrumental": true, "model": "V6", "title": "Norfolk - Contact",
    "style": "dark orchestral documentary tension, low taiko pulse, sustained strings, sparse, no vocals",
    "duration": 100 } }
```
```json
{ "model": "ai-music-api/sounds", "input": { "prompt": "distant tank cannon boom with long desert echo, rain", "model": "V6" } }
```

**Polling** (no public callback URL in a cloud session, so poll): `GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=…` → on success, download `resultUrls` straight away. kie deletes files after 14 days. Errors come back as **HTTP 200 with an error `code`**, so always check `code`. Rate limit: 20 new tasks per 10s, so animators submit in waves of 15.

**T0 (free):**
```bash
ffmpeg -loop 1 -i kf/S012.png -vf "scale=7680:-1,zoompan=z='min(zoom+0.0007,1.10)':d=125:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25" -t 5 -c:v libx264 -pix_fmt yuv420p clips/S012.mp4
```

---

## 7. The routine

- **What it is:** a saved Claude Code task in the cloud environment, attached to the `henry-studio` repo. It can run on a schedule, or be fired with `POST https://api.anthropic.com/v1/claude_code/routines/{id}/fire` with an optional text payload. Routines are in research preview, and the API is marked experimental.
- **Saved prompt:**
  > *Read `projects/*/state.json`. For each project whose next stage is unlocked by Henry's approval, run it to the next gate following CLAUDE.md. Respect `budget.max_credits`. Sync assets with rclone, commit text artifacts, and post a summary with contact sheets when you reach the gate.*
- **Henry's loop:** chat → Gate 1 → Gate 2 → *"render it"*. The Showrunner sets `state.json` to `animate` and fires the routine, and the render runs overnight. In the morning Henry opens that routine's session in the Claude app, watches `final.mp4`, and types his notes. Only the affected shots get redone.
- **Resumable:** every task ID and result is written to `state.json`, so a crash or timeout picks up where it stopped. No credits are spent twice.

---

## 8. Setup checklist (what you set up for Henry)

1. **kie.ai account**, then an API key with a **daily credit cap**, plus a $20 top-up for the moderation test.
2. **Claude plan:** routines and long agent runs use subscription usage. A full film is heavy, so **Max** is likely needed (Pro will probably hit limits).
3. **GitHub repo** `henry-studio` with the files above. Connect it to Claude Code on the web.
4. **Cloud environment settings:**
   - secret `KIE_API_KEY` (plus rclone credentials for R2 or Drive)
   - network access to `api.kie.ai`, kie's result file host, `registry.npmjs.org`
   - a setup script that installs `ffmpeg` and `rclone`
5. **Storage:** a Cloudflare R2 bucket or a Google Drive folder. Media never goes into git.
6. **Motion reference library:** 20–30 short stock or self-filmed clips (run, crouch, salute, load, point, radio call) for motion control.

---

## 9. Risks and how they're handled

| Risk | Mitigation |
|---|---|
| **Moderation blocks combat** (Seedance blocks keywords; Kling follows Chinese content rules) | `combat-lexicon.md` (equipment, effects and period words instead of violent verbs), distance framing, no gore. Fallback chain ends at T0. **Step 0: test 20 of Henry's real prompts on each model.** |
| Character drift | sheets + 10-ref keyframes + locked first/last frames + Kling elements + vision QC |
| kie is a reseller (prices change, some integrations break) | `kie.py` fallback client; record `creditsConsumed` per task; `max_credits` caps; switching to fal.ai only changes the endpoint |
| 720p output | ffmpeg lanczos upscale to 1080p, fine for YouTube. Hero shots can use Kling `pro` (18 cr/s) |
| YouTube "low-effort AI" crackdown, X war-video rules | original research, written VO, real editing, AI disclosure label |
| Routine runtime or disk limits | stage-by-stage runs, rclone sync after each wave, resumable `state.json` |

---

## 10. Build order

1. **Day 0, moderation and look test ($20):** 20 combat prompts × Wan Flash / Seedance Mini / Kling 3.0, and 5 cast sheets. Pick defaults based on the results.
2. **Day 1–2:** repo, agents, skill, house rules, `kie.py`, ffmpeg scripts.
3. **Day 3:** 60-second pilot scene end to end. Tune the critic thresholds and prompts.
4. **Day 4:** full 5.5-minute film, then hand over to Henry.
