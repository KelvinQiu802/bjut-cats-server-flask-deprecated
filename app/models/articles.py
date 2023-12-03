from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, INTEGER
from extentions import db


class Articles(db.Model):
    id: Mapped[int] = mapped_column(
        INTEGER, primary_key=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(
        String(255), nullable=False)
    subTitle: Mapped[str] = mapped_column(
        String(255), nullable=False)
    image: Mapped[str] = mapped_column(String(255), nullable=False)
    link: Mapped[str] = mapped_column(String(255), nullable=False)

    def toDict(self) -> dict[str, str]:
        return dict(id=self.id, title=self.title, subTitle=self.subTitle, image=self.image, link=self.link)
