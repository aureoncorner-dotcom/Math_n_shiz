# Probe log analysis

**Result:** After excluding 65 Bound `0.0.0.0:0` rows, the attachment contains 66 unique remote TCP tuples: 60 first seen as Established, 5 as SynSent, and 1 as FinWait1. Codex has concentrated same-endpoint bursts; Chrome has broader endpoint fanout; ChatGPT has only four retained tuples in this excerpt. The observations do not identify requests, hidden workers, or backend causes.

**Source and scope.** `Pasted text.txt`, 14,689 bytes, SHA-256 `3ba7b0833ab195ed5913584c7c15c47ff38b15603749765ca81ba610c085c482`. The displayed event span is 00:09:01.794–00:17:26.226 (504.432 seconds; 8 minutes 24.432 seconds). The attachment has 131 NEW rows, 24 manual markers, 6 BURST alerts, and 11 FANOUT alerts. It does not contain a date/time zone, initial snapshot, stop record, process-start values, or packet capture. Date September 19, 2026 comes from the referenced conversation, not the attachment itself. The two older same-named attachments were not merged into these counts.

**Counting method.** A tuple is process name + PID + local IP:port + remote IP:port. State is preserved separately. All 66 retained tuple keys are unique. Exclude only Bound rows with remote 0.0.0.0:0; do not discard SynSent or FinWait1. The 65 excluded rows each have a retained counterpart with the same process/PID/local port; the Codex FinWait1 tuple on port 51818 is the sole retained tuple without such a Bound counterpart. This match does not by itself prove a socket lifecycle.

Recomputed burst: at least five first-observed unique tuples for the same process/PID and remote IP:port in a trailing, inclusive 3-second window. Recomputed fanout: at least three distinct remote IP:port endpoints for the same process/PID in a trailing, inclusive 30-second window. Windows use the displayed NEW timestamps, not the printed alert counts. They overlap and must not be summed as independent events. All retained local addresses are 192.168.40.7. Remote means the TCP peer field; Chrome's 192.168.40.1:53 is a LAN peer and remains included.

**Process totals.**

| Process / PID | Bound excluded | Retained | Established | SynSent | FinWait1 | Distinct endpoints | Max same-endpoint tuples / 3s | Max endpoints / 30s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| codex.exe / 56004 | 38 | 39 | 36 | 2 | 1 | 2 | 10 | 1 |
| ChatGPT.exe / 3868 | 4 | 4 | 4 | 0 | 0 | 4 | 1 | 2 |
| chrome.exe / 30064 | 23 | 23 | 20 | 3 | 0 | 12 | 4 | 7 |

Established-only same-endpoint 3-second maxima are Codex 9, ChatGPT 1, Chrome 2. Across all endpoints within each process, the 3-second tuple maxima are Codex 10, ChatGPT 1, Chrome 4. Only Codex reaches the five-tuple burst threshold; only Chrome reaches the three-endpoint fanout threshold.

**Codex concentration and bursts.** 33 of 39 retained tuples (84.615%) target 104.18.32.47:443; the other six target 172.64.155.209:443. For the former, states are 30 Established, 2 SynSent, and 1 FinWait1; all six for the latter are Established. The six 172.64.155.209 tuples span 00:15:36.645–00:16:00.165 (23.520 seconds), and their largest 3-second count is only three. The two destinations do not co-occur in any trailing 30-second window of first-observed rows.

| Representative qualifying window (first–last member) | Count | Observed states | Member span | Nearest marker to first member | First member − marker |
| --- | --- | --- | --- | --- | --- |
| 00:16:55.373–00:16:58.278 | 10 | 9 Established + 1 SynSent | 2.905 s | 00:16:55.703 | -0.330 s |
| 00:16:58.278–00:17:01.130 | 6 | 5 Established + 1 SynSent | 2.852 s | 00:16:55.703 | +2.575 s |
| 00:16:59.701–00:17:02.542 | 6 | 6 Established | 2.841 s | 00:16:55.703 | +3.998 s |
| 00:17:14.100–00:17:14.167 | 10 | 8 Established + 1 SynSent + 1 FinWait1 | 0.067 s | 00:16:55.703 | +18.397 s |

The first window contains nine Established rows printed in 61 ms (00:16:55.373–55.434), followed by one SynSent row at 58.278. The next two rows in the table are overlapping views of the continuing sequence: one has five Established plus that SynSent tuple, and the other has six Established. In total, 00:16:55.373–00:17:02.542 contains 16 unique tuples (15 Established, 1 SynSent) over 7.169 seconds, not 22 independent tuples from adding overlapping windows.

The later dense group at 00:17:14.100–14.167 contains 10 unique tuples: 8 Established, 1 SynSent (port 51821), and 1 FinWait1 (port 51818). Its 67 ms print span is not a measured connection-creation duration. Subsequent groups are three Established tuples at 00:17:20.326–20.340 and one at 00:17:26.226; neither qualifies as a five-tuple/3-second burst.

**Printed burst alert audit.** Three alerts target 0.0.0.0:0 and are discarded. The remaining three target 104.18.32.47:443. Each prints when its running count reaches five; the count is not the eventual group size.

| Alert timestamp | States counted at alert | Nearest marker | Alert − marker |
| --- | --- | --- | --- |
| 00:16:55.408 | 5 Established | 00:16:55.703 | -0.295 s |
| 00:16:59.729 | 4 Established + 1 SynSent | 00:16:55.703 | +4.026 s |
| 00:17:14.134 | 3 Established + 1 SynSent + 1 FinWait1 | 00:16:55.703 | +18.431 s |

The later burst alerts include non-Established states. The 00:16:59.729 alert is 4 Established + 1 SynSent; the 00:17:14.134 alert is 3 Established + 1 SynSent + 1 FinWait1. A claim that each alert establishes five newly connected sockets would be wrong.

**Chrome and ChatGPT.** Chrome's largest same-endpoint group is four tuples to the LAN peer 192.168.40.1:53 at 00:15:01.476–01.495: two Established and two SynSent. Its eight tuples to that LAN endpoint comprise five Established and three SynSent. The other 15 Chrome tuples are Established and target 11 non-LAN endpoints. No Chrome window reaches five same-endpoint tuples.

Chrome does reach seven genuine endpoints in a 30-second window ending 00:14:45.027, with member observations from 00:14:15.229 through 00:14:45.027 (29.798 seconds), all Established: 140.82.113.22:443, 23.223.33.24:443, 140.82.114.25:443, 140.82.113.5:443, 185.199.108.133:443, 140.82.114.4:443, and 140.82.114.26:443. Its first corrected fanout threshold crossing is 00:13:49.710. The peak-window endpoint observation at 00:14:45.027 is +7.899 seconds from its nearest marker, 00:14:37.128.

ChatGPT's four Established tuples go to four endpoints across the full excerpt, but at most two occur within any 30 seconds. The 00:16:52.527 three-remote alert includes the Bound artifact; its actual peers in that window are 64.239.109.1:443 (00:16:30.662) and 35.190.80.1:443 (00:16:52.519). Thus ChatGPT has neither a qualifying five-tuple burst nor a three-endpoint fanout in this excerpt.

**Every printed fanout alert contains an artifact endpoint.** At the instant of the alert, every printed endpoint count falls by one. Some alerts occur before the corresponding real NEW row is printed, so recomputed fanout can increase a few milliseconds later. This is why Chrome's printed seven at 00:14:45.018 corrects to six at that instant, yet the next NEW row at 00:14:45.027 brings the genuine total to seven.

| Alert time | Process | Printed endpoints | Real endpoints at alert | Meets ≥3 after correction? |
| --- | --- | --- | --- | --- |
| 00:13:33.225 | chrome.exe | 3 | 2 | No |
| 00:13:49.698 | chrome.exe | 3 | 2 | No |
| 00:13:55.221 | chrome.exe | 5 | 4 | Yes |
| 00:14:15.221 | chrome.exe | 4 | 3 | Yes |
| 00:14:23.210 | chrome.exe | 3 | 2 | No |
| 00:14:35.499 | chrome.exe | 3 | 2 | No |
| 00:14:45.018 | chrome.exe | 7 | 6 | Yes |
| 00:15:01.451 | chrome.exe | 6 | 5 | Yes |
| 00:15:27.155 | chrome.exe | 3 | 2 | No |
| 00:15:50.267 | chrome.exe | 3 | 2 | No |
| 00:16:52.527 | ChatGPT.exe | 3 | 2 | No |

**Marker timing.** There are 24 markers, all labeled CALL MARKER without an event description. Nearest means the smallest absolute displayed-time distance, with signed offset = observation time − marker time. Negative means before the marker. No marker is an independently verified call start, request, or response event.

Examples: ChatGPT at 00:11:30.170 is −0.258 seconds from 00:11:30.428. ChatGPT at 00:16:52.519 is −0.272 seconds from 00:16:52.791. The first Codex dense group starts at 00:16:55.373, +2.582 seconds after marker 00:16:52.791 but −0.330 seconds before the nearer marker 00:16:55.703. The first nine Established rows finish −0.269 seconds before that nearer marker. The later group starts at 00:17:14.100, +18.397 seconds after the final marker. Marker proximity varies, and nearest-marker selection does not establish a directional or causal association.

**What is established.** The excerpt supports a local observation of concentrated Codex tuple activity to two endpoints over the whole excerpt, broader Chrome endpoint diversity, and sparse observed ChatGPT tuples. Codex has a genuine first-observation burst pattern after Bound artifacts are removed. The log does not identify application requests, users, worker counts, backend topology, DNS names, HTTP exchanges, or reasons for the activity. Four ChatGPT observations are insufficient for a general app-level behavioral baseline. The user's earlier statement that no call was active is contextual self-report, not an interval label encoded in this log; it cannot produce a controlled idle-versus-interaction comparison here.

**Measurement limits from the probe source.** The PowerShell source provided in Self Description uses Get-NetTCPConnection polling, then enumerates processes and writes each row and alert sequentially. A nominal 250 ms sleep is added after each cycle; this is not a verified 250 ms sampling interval. Rows from one enumeration can be printed milliseconds apart. The script timestamps a NEW line during output, runs the alert calculation afterward, and checks the marker key at the start of the next cycle. It provides neither socket creation timestamps nor per-snapshot identifiers. This ordering can itself place markers shortly after batches. The subsecond offsets above are exact arithmetic on displayed timestamps, not measured user-action latency or wire-level timing.

The source seeds already-open tuples and maintains a permanent Seen set whose key excludes state. Consequently the excerpt omits the initial inventory, existing-connection traffic, same-tuple state transitions, and reused tuple keys already seen earlier in a run. It can also miss short-lived connections between polls. Process start is included in the script's internal identity but omitted from the pasted output, so this analysis cannot check process-instance identity across a restart. Counts describe first-observed tuple rows in the supplied excerpt, not all traffic, concurrent connection counts, or complete successful connection counts.

`Established` denotes an open TCP connection at observation; `SynSent` denotes the connection-establishment phase; `FinWait1` denotes a closing phase. A SynSent row is not evidence of eventual success, and a FinWait1 row is not a newly observed handshake completion. These state meanings follow [RFC 9293 §3.3.2](https://www.rfc-editor.org/rfc/rfc9293.html#section-3.3.2).

**All retained rows and nearest markers.** Source line numbers refer to the unchanged attachment. Local IP is 192.168.40.7 throughout. This table retains state and PID; no alert is counted as an extra tuple.

| Source line | Time | Process/PID | Local port | Remote endpoint | State | Nearest marker | Offset (s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 00:09:01.831 | chrome.exe/30064 | 62022 | 162.247.243.29:443 | Established | 00:09:58.185 | -56.354 |
| 5 | 00:09:04.497 | codex.exe/56004 | 53049 | 104.18.32.47:443 | Established | 00:09:58.185 | -53.688 |
| 15 | 00:11:30.170 | ChatGPT.exe/3868 | 60486 | 64.239.123.193:443 | Established | 00:11:30.428 | -0.258 |
| 22 | 00:13:33.205 | chrome.exe/30064 | 59915 | 34.51.10.38:443 | Established | 00:14:14.166 | -40.961 |
| 23 | 00:13:33.211 | chrome.exe/30064 | 52757 | 162.247.243.29:443 | Established | 00:14:14.166 | -40.955 |
| 29 | 00:13:33.231 | chrome.exe/30064 | 49364 | 34.51.10.38:443 | Established | 00:14:14.166 | -40.935 |
| 37 | 00:13:49.710 | chrome.exe/30064 | 59945 | 140.82.113.22:443 | Established | 00:14:14.166 | -24.456 |
| 38 | 00:13:49.717 | chrome.exe/30064 | 57224 | 140.82.114.4:443 | Established | 00:14:14.166 | -24.449 |
| 48 | 00:13:55.236 | chrome.exe/30064 | 62109 | 192.168.40.1:53 | Established | 00:14:14.166 | -18.930 |
| 49 | 00:13:55.243 | chrome.exe/30064 | 61369 | 192.168.40.1:53 | SynSent | 00:14:14.166 | -18.923 |
| 58 | 00:14:15.229 | chrome.exe/30064 | 49702 | 140.82.113.22:443 | Established | 00:14:14.166 | +1.063 |
| 66 | 00:14:23.219 | chrome.exe/30064 | 57191 | 23.223.33.24:443 | Established | 00:14:16.798 | +6.421 |
| 76 | 00:14:35.519 | chrome.exe/30064 | 64756 | 140.82.114.25:443 | Established | 00:14:34.387 | +1.132 |
| 77 | 00:14:35.524 | chrome.exe/30064 | 63166 | 140.82.113.5:443 | Established | 00:14:34.387 | +1.137 |
| 78 | 00:14:35.532 | chrome.exe/30064 | 57669 | 185.199.108.133:443 | Established | 00:14:34.387 | +1.145 |
| 81 | 00:14:38.250 | chrome.exe/30064 | 53148 | 140.82.114.4:443 | Established | 00:14:37.128 | +1.122 |
| 92 | 00:14:45.027 | chrome.exe/30064 | 57292 | 140.82.114.26:443 | Established | 00:14:37.128 | +7.899 |
| 108 | 00:15:01.476 | chrome.exe/30064 | 64729 | 192.168.40.1:53 | Established | 00:15:01.763 | -0.287 |
| 109 | 00:15:01.483 | chrome.exe/30064 | 58626 | 192.168.40.1:53 | SynSent | 00:15:01.763 | -0.280 |
| 110 | 00:15:01.489 | chrome.exe/30064 | 51734 | 192.168.40.1:53 | SynSent | 00:15:01.763 | -0.274 |
| 111 | 00:15:01.495 | chrome.exe/30064 | 49704 | 192.168.40.1:53 | Established | 00:15:01.763 | -0.268 |
| 117 | 00:15:27.148 | chrome.exe/30064 | 57743 | 104.18.32.47:443 | Established | 00:15:20.610 | +6.538 |
| 124 | 00:15:35.303 | ChatGPT.exe/3868 | 50182 | 64.233.178.139:443 | Established | 00:15:20.610 | +14.693 |
| 126 | 00:15:36.645 | codex.exe/56004 | 50183 | 172.64.155.209:443 | Established | 00:15:20.610 | +16.035 |
| 128 | 00:15:42.044 | codex.exe/56004 | 56393 | 172.64.155.209:443 | Established | 00:15:20.610 | +21.434 |
| 131 | 00:15:46.165 | codex.exe/56004 | 60497 | 172.64.155.209:443 | Established | 00:15:20.610 | +25.555 |
| 132 | 00:15:46.172 | codex.exe/56004 | 60495 | 172.64.155.209:443 | Established | 00:15:20.610 | +25.562 |
| 134 | 00:15:48.891 | codex.exe/56004 | 60501 | 172.64.155.209:443 | Established | 00:15:20.610 | +28.281 |
| 137 | 00:15:50.260 | chrome.exe/30064 | 58521 | 192.168.40.1:53 | Established | 00:15:20.610 | +29.650 |
| 143 | 00:15:50.273 | chrome.exe/30064 | 50060 | 192.168.40.1:53 | Established | 00:15:20.610 | +29.663 |
| 145 | 00:15:51.653 | chrome.exe/30064 | 64848 | 74.125.197.139:443 | Established | 00:15:20.610 | +31.043 |
| 147 | 00:16:00.165 | codex.exe/56004 | 49356 | 172.64.155.209:443 | Established | 00:15:20.610 | +39.555 |
| 149 | 00:16:30.662 | ChatGPT.exe/3868 | 60814 | 64.239.109.1:443 | Established | 00:16:52.791 | -22.129 |
| 151 | 00:16:37.524 | codex.exe/56004 | 60818 | 104.18.32.47:443 | Established | 00:16:52.791 | -15.267 |
| 153 | 00:16:41.612 | codex.exe/56004 | 60822 | 104.18.32.47:443 | Established | 00:16:52.791 | -11.179 |
| 155 | 00:16:52.519 | ChatGPT.exe/3868 | 61925 | 35.190.80.1:443 | Established | 00:16:52.791 | -0.272 |
| 173 | 00:16:55.373 | codex.exe/56004 | 61941 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.330 |
| 174 | 00:16:55.381 | codex.exe/56004 | 61936 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.322 |
| 175 | 00:16:55.388 | codex.exe/56004 | 61935 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.315 |
| 176 | 00:16:55.395 | codex.exe/56004 | 61934 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.308 |
| 177 | 00:16:55.402 | codex.exe/56004 | 61933 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.301 |
| 180 | 00:16:55.414 | codex.exe/56004 | 61932 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.289 |
| 181 | 00:16:55.421 | codex.exe/56004 | 61931 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.282 |
| 182 | 00:16:55.427 | codex.exe/56004 | 61930 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.276 |
| 183 | 00:16:55.434 | codex.exe/56004 | 61929 | 104.18.32.47:443 | Established | 00:16:55.703 | -0.269 |
| 186 | 00:16:58.278 | codex.exe/56004 | 61945 | 104.18.32.47:443 | SynSent | 00:16:55.703 | +2.575 |
| 193 | 00:16:59.701 | codex.exe/56004 | 61954 | 104.18.32.47:443 | Established | 00:16:55.703 | +3.998 |
| 194 | 00:16:59.708 | codex.exe/56004 | 61949 | 104.18.32.47:443 | Established | 00:16:55.703 | +4.005 |
| 195 | 00:16:59.715 | codex.exe/56004 | 61948 | 104.18.32.47:443 | Established | 00:16:55.703 | +4.012 |
| 196 | 00:16:59.721 | codex.exe/56004 | 61946 | 104.18.32.47:443 | Established | 00:16:55.703 | +4.018 |
| 200 | 00:17:01.130 | codex.exe/56004 | 61961 | 104.18.32.47:443 | Established | 00:16:55.703 | +5.427 |
| 202 | 00:17:02.542 | codex.exe/56004 | 61972 | 104.18.32.47:443 | Established | 00:16:55.703 | +6.839 |
| 214 | 00:17:14.100 | codex.exe/56004 | 51821 | 104.18.32.47:443 | SynSent | 00:16:55.703 | +18.397 |
| 215 | 00:17:14.107 | codex.exe/56004 | 51818 | 104.18.32.47:443 | FinWait1 | 00:16:55.703 | +18.404 |
| 216 | 00:17:14.114 | codex.exe/56004 | 51815 | 104.18.32.47:443 | Established | 00:16:55.703 | +18.411 |
| 217 | 00:17:14.120 | codex.exe/56004 | 51814 | 104.18.32.47:443 | Established | 00:16:55.703 | +18.417 |
| 218 | 00:17:14.127 | codex.exe/56004 | 51813 | 104.18.32.47:443 | Established | 00:16:55.703 | +18.424 |
| 221 | 00:17:14.139 | codex.exe/56004 | 51812 | 104.18.32.47:443 | Established | 00:16:55.703 | +18.436 |
| 222 | 00:17:14.146 | codex.exe/56004 | 51811 | 104.18.32.47:443 | Established | 00:16:55.703 | +18.443 |
| 223 | 00:17:14.154 | codex.exe/56004 | 51810 | 104.18.32.47:443 | Established | 00:16:55.703 | +18.451 |
| 224 | 00:17:14.160 | codex.exe/56004 | 51809 | 104.18.32.47:443 | Established | 00:16:55.703 | +18.457 |
| 225 | 00:17:14.167 | codex.exe/56004 | 51808 | 104.18.32.47:443 | Established | 00:16:55.703 | +18.464 |
| 229 | 00:17:20.326 | codex.exe/56004 | 51844 | 104.18.32.47:443 | Established | 00:16:55.703 | +24.623 |
| 230 | 00:17:20.333 | codex.exe/56004 | 51833 | 104.18.32.47:443 | Established | 00:16:55.703 | +24.630 |
| 231 | 00:17:20.340 | codex.exe/56004 | 51832 | 104.18.32.47:443 | Established | 00:16:55.703 | +24.637 |
| 233 | 00:17:26.226 | codex.exe/56004 | 51858 | 104.18.32.47:443 | Established | 00:16:55.703 | +30.523 |

**Every marker's nearest retained observation by process.** This is the inverse lookup, separate from each event's nearest marker. Cells show observation time (signed observation − marker offset); multiple markers may share the same nearest observation. Those matches are not independent trials.

| Marker time | Codex nearest observation | ChatGPT nearest observation | Chrome nearest observation |
| --- | --- | --- | --- |
| 00:09:58.185 | 00:09:04.497 (-53.688 s) | 00:11:30.170 (+91.985 s) | 00:09:01.831 (-56.354 s) |
| 00:10:04.032 | 00:09:04.497 (-59.535 s) | 00:11:30.170 (+86.138 s) | 00:09:01.831 (-62.201 s) |
| 00:10:42.806 | 00:09:04.497 (-98.309 s) | 00:11:30.170 (+47.364 s) | 00:09:01.831 (-100.975 s) |
| 00:10:48.492 | 00:09:04.497 (-103.995 s) | 00:11:30.170 (+41.678 s) | 00:09:01.831 (-106.661 s) |
| 00:11:22.716 | 00:09:04.497 (-138.219 s) | 00:11:30.170 (+7.454 s) | 00:13:33.205 (+130.489 s) |
| 00:11:26.546 | 00:09:04.497 (-142.049 s) | 00:11:30.170 (+3.624 s) | 00:13:33.205 (+126.659 s) |
| 00:11:27.843 | 00:09:04.497 (-143.346 s) | 00:11:30.170 (+2.327 s) | 00:13:33.205 (+125.362 s) |
| 00:11:29.122 | 00:09:04.497 (-144.625 s) | 00:11:30.170 (+1.048 s) | 00:13:33.205 (+124.083 s) |
| 00:11:30.428 | 00:09:04.497 (-145.931 s) | 00:11:30.170 (-0.258 s) | 00:13:33.205 (+122.777 s) |
| 00:11:42.991 | 00:09:04.497 (-158.494 s) | 00:11:30.170 (-12.821 s) | 00:13:33.205 (+110.214 s) |
| 00:11:53.850 | 00:09:04.497 (-169.353 s) | 00:11:30.170 (-23.680 s) | 00:13:33.205 (+99.355 s) |
| 00:14:14.166 | 00:15:36.645 (+82.479 s) | 00:15:35.303 (+81.137 s) | 00:14:15.229 (+1.063 s) |
| 00:14:16.798 | 00:15:36.645 (+79.847 s) | 00:15:35.303 (+78.505 s) | 00:14:15.229 (-1.569 s) |
| 00:14:34.387 | 00:15:36.645 (+62.258 s) | 00:15:35.303 (+60.916 s) | 00:14:35.519 (+1.132 s) |
| 00:14:37.128 | 00:15:36.645 (+59.517 s) | 00:15:35.303 (+58.175 s) | 00:14:38.250 (+1.122 s) |
| 00:14:54.930 | 00:15:36.645 (+41.715 s) | 00:15:35.303 (+40.373 s) | 00:15:01.476 (+6.546 s) |
| 00:14:59.006 | 00:15:36.645 (+37.639 s) | 00:15:35.303 (+36.297 s) | 00:15:01.476 (+2.470 s) |
| 00:15:00.342 | 00:15:36.645 (+36.303 s) | 00:15:35.303 (+34.961 s) | 00:15:01.476 (+1.134 s) |
| 00:15:01.763 | 00:15:36.645 (+34.882 s) | 00:15:35.303 (+33.540 s) | 00:15:01.495 (-0.268 s) |
| 00:15:03.137 | 00:15:36.645 (+33.508 s) | 00:15:35.303 (+32.166 s) | 00:15:01.495 (-1.642 s) |
| 00:15:15.287 | 00:15:36.645 (+21.358 s) | 00:15:35.303 (+20.016 s) | 00:15:27.148 (+11.861 s) |
| 00:15:20.610 | 00:15:36.645 (+16.035 s) | 00:15:35.303 (+14.693 s) | 00:15:27.148 (+6.538 s) |
| 00:16:52.791 | 00:16:55.373 (+2.582 s) | 00:16:52.519 (-0.272 s) | 00:15:51.653 (-61.138 s) |
| 00:16:55.703 | 00:16:55.434 (-0.269 s) | 00:16:52.519 (-3.184 s) | 00:15:51.653 (-64.050 s) |

**All endpoint counts.**

| Process | Endpoint | Retained tuples | Observed states |
| --- | --- | --- | --- |
| codex.exe | 104.18.32.47:443 | 33 | 30 Established + 2 SynSent + 1 FinWait1 |
| codex.exe | 172.64.155.209:443 | 6 | 6 Established |
| ChatGPT.exe | 64.239.123.193:443 | 1 | 1 Established |
| ChatGPT.exe | 64.233.178.139:443 | 1 | 1 Established |
| ChatGPT.exe | 64.239.109.1:443 | 1 | 1 Established |
| ChatGPT.exe | 35.190.80.1:443 | 1 | 1 Established |
| chrome.exe | 162.247.243.29:443 | 2 | 2 Established |
| chrome.exe | 34.51.10.38:443 | 2 | 2 Established |
| chrome.exe | 140.82.113.22:443 | 2 | 2 Established |
| chrome.exe | 140.82.114.4:443 | 2 | 2 Established |
| chrome.exe | 192.168.40.1:53 | 8 | 5 Established + 3 SynSent |
| chrome.exe | 23.223.33.24:443 | 1 | 1 Established |
| chrome.exe | 140.82.114.25:443 | 1 | 1 Established |
| chrome.exe | 140.82.113.5:443 | 1 | 1 Established |
| chrome.exe | 185.199.108.133:443 | 1 | 1 Established |
| chrome.exe | 140.82.114.26:443 | 1 | 1 Established |
| chrome.exe | 104.18.32.47:443 | 1 | 1 Established |
| chrome.exe | 74.125.197.139:443 | 1 | 1 Established |

**Verification.** Every NEW and MARK line parsed; no duplicate retained tuple key. Arithmetic reconciles 131 = 65 + 66 and 66 = 60 Established + 5 SynSent + 1 FinWait1. Original source preserved unchanged. All source-row references, filters, rolling-window members, alert corrections, and offsets are also supplied in `probe-analysis.json`.

