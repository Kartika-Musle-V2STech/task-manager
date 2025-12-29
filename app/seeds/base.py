from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def get_or_create(db:Session, model, defaults=None, **filters):
    """
    get an existing row matchin filters or create it.
    """
    instance = db.query(model).filter_by(**filters).first()
    if instance:
        return instance

    params = dict(filters)
    if defaults:
        params.update(defaults)

    instance = model(**params)
    db.add(instance)

    try: 
       db.commit()
    except IntegrityError:
        db.rollback()
        return db.query(model).filter_by(**filters).first()
        
    db.refresh(instance)
    return instance