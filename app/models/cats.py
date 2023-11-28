from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, INTEGER, Enum, TEXT, FLOAT
from extentions import db


class Cats(db.Model):
    id: Mapped[int] = mapped_column(
        INTEGER, nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    campus: Mapped[str] = mapped_column(
        Enum('本部', '中篮', '通州'), nullable=False, primary_key=True
    )
    avatar: Mapped[str] = mapped_column(
        TEXT, nullable=True
    )
    gender: Mapped[str] = mapped_column(
        Enum('公', '母', '未知'), nullable=False
    )
    color: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    hair: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    neutered: Mapped[str] = mapped_column(
        Enum('已绝育', '未绝育', '未知'), nullable=False
    )
    state: Mapped[str] = mapped_column(
        Enum('在校', '毕业', '休学', '喵星'), nullable=False
    )
    description: Mapped[str] = mapped_column(
        TEXT, nullable=True
    )
    birthday: Mapped[str] = mapped_column(
        String(255), nullable=True
    )
    adoptionDay: Mapped[str] = mapped_column(
        String(255), nullable=True
    )
    position: Mapped[str] = mapped_column(
        TEXT, nullable=True
    )
    longitude: Mapped[float] = mapped_column(
        FLOAT, nullable=True
    )
    latitude: Mapped[float] = mapped_column(
        FLOAT, nullable=True
    )
    orderWeight: Mapped[int] = mapped_column(
        INTEGER, nullable=True
    )
    image: Mapped[str] = mapped_column(
        TEXT, nullable=True
    )

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'campus': self.campus,
            'avatar': self.avatar,
            'gender': self.gender,
            'color': self.color,
            'hair': self.hair,
            'neutered': self.neutered,
            'state': self.state,
            'description': self.description,
            'birthday': self.birthday,
            'adoptionDay': self.adoptionDay,
            'position': self.position,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'orderWeight': self.orderWeight,
            'image': self.image,
        }
