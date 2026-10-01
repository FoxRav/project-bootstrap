---
name: domain-modeling
description: "Define domain vocabulary, entities, states and business invariants when terminology or conceptual relationships are unclear."
---

# domain-modeling

## Purpose

Give people, specifications and tests a consistent conceptual language.

## Use when

A domain-heavy feature introduces new concepts, a term has multiple meanings, or behavior depends on unclear business rules.

## Do not use when

A mechanical change introduces no domain meaning. Database tables and code class design alone belong in architecture/specification work.

## Required context

Read the domain/glossary location mapped by [project context](../../docs/PROJECT.md), affected requirements, representative code/tests and relevant confirmed Product Owner decisions.

## Inputs

Representative scenarios, disputed terms, business constraints and the domain decision owner.

## Process

1. Extract terms from actual scenarios and sources. Separate business concepts from accidental implementation names.
2. Identify entities and identity, value concepts, lifecycle states, relationships/cardinality, ownership and business rules.
3. State invariants and valid/invalid transitions using examples and counterexamples; distinguish observed behavior from intended rules.
4. Resolve aliases and synonyms to preferred terms. Record forbidden ambiguous terminology and its replacement with a reason.
5. Ask only unresolved domain choices. Mark provisional definitions explicitly rather than inventing business facts.
6. Update the existing glossary or project terminology section with confirmed definitions and linked rules. Use a small diagram/table when it clarifies relationships; keep storage, APIs and class layouts in their proper sources.

## Decision points

Extract a separate glossary only when size warrants it. If evidence conflicts with accepted business intent, use the conflict procedure before changing behavior.

## Approval boundaries

Read and apply the [shared contract](../README.md#shared-contract). A conceptual model does not authorize persistent schema, public contract or business-policy changes.

## Outputs

A coherent vocabulary and conceptual model covering concepts, entities, states, relationships, invariants, aliases, ambiguous terms and business rules.

## Completion criteria

The affected scenarios can be described without conflicting terms; confirmed definitions and open questions have clear sources and owners.

## Evidence

Link definitions to decisions and example scenarios; record unresolved contradictions and terminology checks against affected documents.

## Handoff

Provide the glossary links and business invariants to to-spec, architecture-review and test authors as needed.
