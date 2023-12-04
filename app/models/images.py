from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, ForeignKey
from extentions import db


class Images(db.Model):
    openId: Mapped[str] = mapped_column(
        String(255), ForeignKey('users.openId',
                                ondelete='cascade', onupdate='cascade'),
        nullable=False)
    imageUrl: Mapped[str] = mapped_column(
        String(255), nullable=False, primary_key=True)
    state: Mapped[str] = mapped_column(
        Enum('待审核', '通过', '不通过', '精选'), nullable=False)
    campus: Mapped[str] = mapped_column(
        Enum('本部', '通州', '中篮'), nullable=False)
    catName: Mapped[str] = mapped_column(
        String(255), nullable=False)

    def toDict(self) -> dict[str, str]:
        return dict(openId=self.openId, imageUrl=self.imageUrl, state=self.state, campus=self.campus, catName=self.catName)
