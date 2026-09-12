**GUI SRT** is system response time in a graphical interface: the gap from a user act to the first usable on-screen consequence of that act.

## Clock

Start: key down, click down, or tap — the moment the user committed.

Stop: the first update they can use (character appears, list populates, button state changes, caret moves). Not “the HTTP 200,” not “the spinner started,” not server RTT.

That interval is one SRT. A session is a sequence of them. \(\mu\) and \(\sigma\) in the exchange-rate card are summary stats of that sequence, on this clock.

Weber, Haering, Thomaschke (2013) used **SRT** in that sense on sequential office software: the program paused after an action for a controlled duration before the next widget was ready. They lengthened the *short* pauses so the set of durations shrank. Mean SRT went up; people answered the next step faster.

## What it is not

| Term | Clock |
|---|---|
| Network RTT / ping | packet out and back |
| Server latency | request received → response sent |
| Time to first byte | connection → first byte |
| Frame time / input lag (games) | input → pose / photon (Normoyle / TAP live here) |
| Token latency | key → first new token on screen (closer to SRT if the UI is a transcript) |
| GUI SRT | action → usable widget change |

A fast backend with a slow paint still has a long SRT. A padded UI with a fast backend has a longer SRT *on purpose*.

## Why \(\sigma\) shows up

Sequential GUI work is a chain of SRTs. The user prepares the next click in the gap. A mix of 40 ms and 400 ms wrecks that preparation (*when*). A metronome at 180 ms restores *when* and costs \(\mu\). A duration that means “this button vs that button” is *which* (Thomaschke), not an SRT pad.

Progress spinners, skeleton screens, and “instant” optimistic UI are representation maps: they change what counts as the stop event. If the spinner is not usable, it is not the SRT stop. \(A_{\mathrm{sel}}\) can look instant while \(A_{\mathrm{task}}\) is still waiting on the real widget. That is the v2.1 split.

## How you would run the factorial on this \(D\)

1. Instrument action onset and first usable paint (not DevTools TTFB).
2. Pick a sequential task with many SRTs (mail triage, form, file ops) — Weber’s setting.
3. Operator: pad shorts to a ceiling, or a fixed metronome. Do not also encode the next screen in the wait unless that is the claim.
4. Primary \(W\): next-action RT, task time, or errors — pick one. Ratings are secondary (Weber: UX stayed flat while RT moved).
5. \(\Delta\): named extra mean vs named leftover \(\sigma\).

Transfer to FPS or tokens is D4: different \(D\).

## One line

GUI SRT is the user-action-to-usable-widget interval in a desktop or web UI. The exchange-rate pad on that \(D\) is Weber: lengthen short SRTs, accept a higher mean, test whether people move sooner. It is not ping and not a game pose clock.
