"""task status and priority enums

Revision ID: e5fbafe1f301
Revises: 8fefd37cdff2
Create Date: 2025-12-27
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e5fbafe1f301"
down_revision = "8fefd37cdff2"
branch_labels = None
depends_on = None


def upgrade():
    """
    Convert task status and priority from FK-based lookup
    columns to ENUM columns (SQLite-safe).
    """
    with op.batch_alter_table("tasks") as batch_op:
        batch_op.add_column(
            sa.Column(
                "status",
                sa.Enum(
                    "pending",
                    "ongoing",
                    "completed",
                    "cancelled",
                    name="task_status_enum",
                ),
                nullable=False,
                server_default="pending",
            )
        )

        batch_op.add_column(
            sa.Column(
                "priority",
                sa.Enum(
                    "low",
                    "medium",
                    "high",
                    name="task_priority_enum",
                ),
                nullable=False,
                server_default="medium",
            )
        )

        # remove old FK-backed columns
        batch_op.drop_column("status_id")
        batch_op.drop_column("priority_id")

    # remove defaults after backfill
    with op.batch_alter_table("tasks") as batch_op:
        batch_op.alter_column("status", server_default=None)
        batch_op.alter_column("priority", server_default=None)


def downgrade():
    """
    Revert ENUM columns back to FK-based integer columns.
    """
    with op.batch_alter_table("tasks") as batch_op:
        batch_op.add_column(
            sa.Column("status_id", sa.Integer(), nullable=False)
        )
        batch_op.add_column(
            sa.Column("priority_id", sa.Integer(), nullable=False)
        )

        batch_op.drop_column("priority")
        batch_op.drop_column("status")