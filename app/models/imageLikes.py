from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, ForeignKey, DATETIME
from extentions import db
from datetime import datetime


class ImageLikes(db.Model):
    openId: Mapped[str] = mapped_column(
        String(255), ForeignKey('users.openId',
                                ondelete='cascade', onupdate='cascade'),
        nullable=False, primary_key=True)
    imageUrl: Mapped[str] = mapped_column(
        String(255), ForeignKey('images.imageUrl', ondelete='cascade', onupdate='cascade'), nullable=False, primary_key=True)
    time: Mapped[datetime] = mapped_column(
        DATETIME, default=datetime.utcnow(), nullable=False)

    def toDict(self) -> dict[str, str]:
        return dict(openId=self.openId, imageUrl=self.imageUrl, time=self.time)
