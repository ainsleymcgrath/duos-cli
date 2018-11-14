from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


def build_schema_from_metadata(metadata, engine):
    """wrapper for database definitions. consider it config."""

    Base = declarative_base()

    Table(
        "article",
        metadata,
        # integer pk interpreted as SERIAL by default
        Column("article_id", Integer, primary_key=True),
        Column("article_title", String, nullable=False),
        Column("duos_label", String, nullable=False),
    )

    Table(
        "author",
        metadata,
        Column("author_id", Integer, primary_key=True),
        Column("author_name", String, nullable=False),
        Column("email_address", String, nullable=True),
    )

    Table(
        "dataset",
        metadata,
        Column("dataset_id", Integer, primary_key=True),
        Column("dataset_name", String, nullable=False),
        Column("abbreviation", String),
    )

    Table(
        "writes",
        metadata,
        Column("writes_id", Integer, primary_key=True),
        Column("article_id", Integer, ForeignKey("article.article_id"), nullable=False),
        Column("author_id", Integer, ForeignKey("author.author_id"), nullable=False),
    )

    Table(
        "reference",
        metadata,
        Column("ref_id", Integer, primary_key=True),
        Column("dataset_id", Integer, ForeignKey("dataset.dataset_id"), nullable=False),
        Column("article_id", Integer, ForeignKey("article.article_id"), nullable=False),
        Column("ref_hash", String, nullable=False),
    )

    Table(
        "validates",
        metadata,
        Column("validation_id", Integer, primary_key=True),
        Column("ref_id", Integer, ForeignKey("reference.ref_id"), nullable=False),
        Column("author_id", Integer, ForeignKey("author.author_id"), nullable=False),
        Column("response", String),
        Column("clarification", String),
        Column("insert_date", DateTime),
        Column("action_date", DateTime),
    )

    return metadata.create_all()
