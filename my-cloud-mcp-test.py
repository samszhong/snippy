# Add chat history if provided
if chat_history:
    logger.info("Adding chat history to thread")
    await project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content=chat_history
    )
