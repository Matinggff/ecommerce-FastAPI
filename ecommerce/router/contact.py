from fastapi import APIRouter, File, UploadFile, Depends, Request, Form, status
from starlette.responses import RedirectResponse
from router.user import templates
from sqlalchemy.orm import Session
from db.datebase import get_db
from db.models import Contact
import datetime
import os

router = APIRouter()


@router.get('/contact_page')
def contact_page(request: Request):
    return templates.TemplateResponse("contact.html",{"request":request})

@router.post('/contact')
def contact(
    db:Session = Depends(get_db),
    name: str = Form(media_type="application/x-www-form-urlencode"),
    email: str = Form(media_type="application/x-www-form-urlencode"),
    massage: str = Form(media_type="application/x-www-form-urlencode"),
    subject: str = Form(media_type="application/x-www-form-urlencode"),
    ):
    
    new_contact = Contact(
    name = name,
    email = email,
    date = datetime.datetime.now(),
    subject = subject,
    massage = massage,
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    url = router.url_path_for('contact_page')
    return RedirectResponse(url,status_code=status.HTTP_303_SEE_OTHER)
 