from app.database.models import async_session
from app.database.models import User, Genre, Art, Cart
from sqlalchemy import select, delete

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_genres():
    async with async_session() as session:
        return await session.scalars(select(Genre))

async def get_genre_arts(genre_id):
    async with async_session() as session:
        return await session.scalars(select(Art).where(Art.genre == genre_id))

async def get_art(art_id):
    async with async_session() as session:
        return await session.scalar(select(Art).where(Art.id == art_id))

async def add_to_cart(tg_id, art_id):
    async with async_session() as session:
        session.add(Cart(user_tg_id=tg_id, art_id=art_id))
        await session.commit()

async def get_cart(tg_id):
    async with async_session() as session:
        return await session.scalars(select(Art).join(Cart).where(Cart.user_tg_id == tg_id))

async def clear_cart(tg_id):
    async with async_session() as session:
        await session.execute(delete(Cart).where(Cart.user_tg_id == tg_id))
        await session.commit()
