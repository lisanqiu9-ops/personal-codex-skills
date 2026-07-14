# Schemas

Use these shapes as working contracts. Add fields only when they improve traceability or later synthesis.

## Chapter Index

```json
{
  "chapter_id": "chapter-001",
  "source_title": "",
  "volume": "",
  "chapter_title": "",
  "spoiler_scope": "this_chapter_only",
  "characters_present": [
    {
      "name": "",
      "aliases": [],
      "role_in_chapter": "",
      "evidence_summary": ""
    }
  ],
  "new_characters": [],
  "factions": [],
  "locations": [],
  "key_events": [
    {
      "event": "",
      "participants": [],
      "consequence": "",
      "evidence_summary": ""
    }
  ],
  "relationship_changes": [
    {
      "source": "",
      "target": "",
      "relationship": "",
      "change": "",
      "confidence": "low|medium|high",
      "evidence_summary": ""
    }
  ],
  "world_terms": [],
  "visual_opportunities": [
    {
      "type": "character|faction|scene|object|relationship",
      "subject": "",
      "visual_value": 1,
      "reason": ""
    }
  ],
  "uncertainties": []
}
```

## Character

```json
{
  "id": "",
  "name": "",
  "aliases": [],
  "first_seen": "",
  "importance": 1,
  "factions": [],
  "roles": [],
  "traits": [],
  "motivations": [],
  "resources_or_abilities": [],
  "conflicts": [],
  "relationships": [],
  "visual_cues": {
    "confirmed": [],
    "inferred": [],
    "invented_for_prompt": []
  },
  "evidence": []
}
```

## Relationship

```json
{
  "source": "",
  "target": "",
  "type": "ally|enemy|mentor|rival|family|romantic|superior|subordinate|unknown",
  "direction": "directed|mutual",
  "status": "stable|changed|uncertain",
  "weight": 1,
  "first_seen": "",
  "latest_evidence": ""
}
```

## Faction

```json
{
  "id": "",
  "name": "",
  "aliases": [],
  "purpose": "",
  "leaders": [],
  "members": [],
  "allies": [],
  "enemies": [],
  "resources": [],
  "visual_identity": [],
  "evidence": []
}
```
