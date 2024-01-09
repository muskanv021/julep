import logging


logger = logging.getLogger(__name__)

create_sessions_relation_query = """
:create sessions {
    session_id: Uuid,
    updated_at: Validity default [floor(now()), true],
    =>
    situation: String,
    summary: String? default null,
    created_at: Float default now(),
}
"""

create_session_lookup_relation_query = """
:create session_lookup {
    agent_id: Uuid,
    user_id: Uuid? default null,
    session_id: Uuid,
}
"""


def init(client):
    sep = "\n}\n\n{\n"
    joined_queries = sep.join(
        [
            create_sessions_relation_query,
            create_session_lookup_relation_query,
        ]
    )

    query = f"{{ {joined_queries} }}"

    try:
        client.run(query)

    except Exception as e:
        logger.exception(e)