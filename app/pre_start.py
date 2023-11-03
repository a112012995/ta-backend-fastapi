import logging
import time

from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


def init() -> None:
    for _ in range(max_tries):
        try:
            db = SessionLocal()
            # Try to create a session to check if the DB is awake
            db.execute("SELECT 1")
            break  # Successful connection, exit the loop
        except Exception as e:
            logger.error(e)
            time.sleep(wait_seconds)
    else:
        # If we reach this point, all attempts have failed
        logger.warning(f"Failed to initialize after {max_tries} attempts")


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
