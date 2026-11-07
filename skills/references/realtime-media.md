# Real-time media

## Purpose

Guide real-time audio/video and interactive media design around measurable experience,
network variability, resource limits and user privacy.

## Use when

A product captures, transmits, relays, records or adapts live audio/video, screen share
or other time-sensitive media.

## Procedure

1. Define user scenarios and measurable quality goals: setup success/time, latency,
   loss, jitter, audio/video continuity, device coverage and recovery. Capture network
   and device conditions; do not invent universal thresholds.
2. Choose peer-to-peer, relay or media-server topology from participant count, network
   reachability, privacy, moderation, recording and cost. Document the topology's
   bandwidth and failure trade-offs.
3. Specify signaling and session lifecycle separately from media transport. Define
   authentication, room membership, authorization, expiry, reconnect and cleanup.
4. For WebRTC, use the selected implementation's current ICE/STUN/TURN and codec
   documentation. Treat ICE candidate addresses as sensitive; authenticate TURN
   credentials and expire them. Do not assume STUN guarantees direct connectivity or
   TURN provides end-to-end media confidentiality from the relay.
5. Define codec negotiation, bitrate adaptation, resolution/frame-rate constraints,
   congestion behavior and fallback based on supported devices and observed link
   quality. Validate compatibility rather than assuming a single codec works everywhere.
6. Make camera/microphone/screen capture explicit, permission-gated and visible to
   users. Define mute/stop behavior, recording/retention consent and handling for
   device permission denial or device changes.
7. Test setup, NAT/firewall reachability, packet loss, jitter, bandwidth restriction,
   reconnect, device changes, participant leave, relay fallback and permissions using
   controlled test clients. Do not expose public IPs, room tokens or media in evidence.
8. Monitor aggregate setup/error/latency/quality and relay use without collecting
   unnecessary content or stable device identifiers. Define session cleanup and
   incident/debug access.

## Decision points

The transport and topology depend on the target browsers/devices and product privacy
model. Encryption in transit does not alone establish end-to-end encryption, recording
consent or safe media retention. TURN relay, SFU and recording services introduce
distinct trust and cost boundaries.

## Approval boundaries

Follow the [shared contract](../README.md#shared-contract), [authority](../../PROJECT_BOOTSTRAP.md#1-authority-and-evidence),
[approval boundaries](../../PROJECT_BOOTSTRAP.md#4-autonomy-and-approval-boundaries),
[quality model](../../PROJECT_BOOTSTRAP.md#5-one-quality-and-completion-model),
[Git authority](../../PROJECT_BOOTSTRAP.md#git-authority) and
[optional review packaging](../../PROJECT_BOOTSTRAP.md#optional-review-packaging).
Media recording, new external services, sensitive telemetry, public session contracts
and production deployment require applicable approval.

## Outputs and evidence

Session/media flow, supported device/network matrix, quality measures, permission and
retention behavior, controlled impairment test results and known coverage gaps. State
which browsers, networks and hardware were not tested.

## Sources

- [W3C WebRTC 1.0: Real-Time Communication Between Browsers](https://www.w3.org/TR/webrtc/), W3C Recommendation; accessed 2026-11-08.
- [RFC 8445, Interactive Connectivity Establishment (ICE)](https://www.rfc-editor.org/rfc/rfc8445.html), accessed 2026-11-08.
- [RFC 8489, Session Traversal Utilities for NAT (STUN)](https://www.rfc-editor.org/rfc/rfc8489.html), accessed 2026-11-08.
- [RFC 8656, Traversal Using Relays around NAT (TURN)](https://www.rfc-editor.org/rfc/rfc8656.html), accessed 2026-11-08.
