# Prompt Templates

Prompts should preserve source facts while separating visual invention from textual evidence.

## Character Prompt

```text
Create a character concept portrait.

Subject: {name}
Story role: {role}
Faction/alignment: {faction}
Personality: {traits}
Motivation: {motivation}
Confirmed visual details: {confirmed_visual_cues}
Inferred visual direction: {inferred_visual_cues}
Invented concept-art details: {invented_details}

Composition: waist-up character portrait, clear face, readable silhouette, no text in image
Style: {style}
Mood: {mood}
Palette: {palette}
Lighting: {lighting}
Background: symbolic environment connected to {location_or_faction}

Avoid: text, watermark, extra limbs, duplicate faces, unrelated modern objects unless specified
```

## Faction Prompt

```text
Create a faction identity poster.

Faction: {name}
Purpose: {purpose}
Core values: {values}
Key members: {members}
Symbols and motifs: {symbols}
Resources or power base: {resources}
Conflict: {main_conflict}

Composition: cinematic group or emblem poster, strong hierarchy, no readable text
Style: {style}
Palette: {palette}
Atmosphere: {atmosphere}

Avoid: logos copied from real brands, text, watermark
```

## Scene Prompt

```text
Create a key scene illustration.

Scene: {scene_summary}
Characters present: {characters}
Location: {location}
Conflict or turning point: {conflict}
Confirmed visual details: {confirmed_visual_details}

Composition: {shot_type}, clear focal point, narrative action visible
Style: {style}
Lighting: {lighting}
Mood: {mood}
Palette: {palette}

Avoid: text, watermark, gore unless user requested and allowed, unrelated characters
```

## Relationship Poster Prompt

```text
Create a relationship-map poster without readable text.

Core character: {core_character}
Major allies: {allies}
Major enemies: {enemies}
Ambiguous relationships: {ambiguous}
Factions: {factions}

Composition: symbolic network poster, central figure, surrounding groups arranged by alliance and conflict, visible emotional distance through pose and lighting
Style: {style}
Palette: {palette}
Mood: {mood}

Avoid: readable labels, tiny faces, cluttered composition, watermark
```
