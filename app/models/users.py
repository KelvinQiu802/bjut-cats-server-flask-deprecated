from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum
from extentions import db


class Users(db.Model):
    openId: Mapped[str] = mapped_column(
        String(255), nullable=False, primary_key=True)
    userName: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(Enum('user', 'admin'), nullable=False)

    def toDict(self) -> dict[str, str]:
        return dict(openId=self.openId, userName=self.userName, role=self.role)
