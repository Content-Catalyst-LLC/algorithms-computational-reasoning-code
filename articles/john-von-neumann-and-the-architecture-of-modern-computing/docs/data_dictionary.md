# Data Dictionary

## architecture_themes.csv

- `theme_id`: interpretive theme in the architecture map.
- `stored_program`: importance of internally stored instructions.
- `memory_organization`: importance of shared symbolic storage and memory structure.
- `control_structure`: importance of sequencing, branching, and execution control.
- `program_as_data`: degree to which programs are treated as stored symbolic objects.
- `implementation_influence`: degree to which architecture shapes real systems.
- `bottleneck_awareness`: degree to which memory movement and bandwidth limits are visible.
- `collaboration_context`: degree to which institutional and collaborative credit is visible.
- `software_relevance`: relevance to compilers, interpreters, operating systems, and software layers.
- `ai_infrastructure`: relevance to scientific computing, simulation, and AI systems.
- `governance_caution`: relevance to security, audit, accountability, and responsible computing.

## von_neumann_architecture_map.csv

- `architecture_score`: average of the theme dimensions.
- `interpretive_status`: core, major, or supporting von Neumann architecture thread.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.
