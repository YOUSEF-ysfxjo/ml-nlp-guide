"""
إرسال الدليل/الموجز بالبريد — مثل research_harvester (EmailNotifier).
يقرأ من متغيرات البيئة: EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT.
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def _markdown_to_html(md: str) -> str:
    """تحويل بسيط من Markdown لـ HTML (عناوين، روابط، أسطر جديدة)."""
    import re
    html = md.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html = re.sub(r"^### (.+)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.+)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^# (.+)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', html)
    html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html)
    html = html.replace("\n\n", "</p><p>").replace("\n", "<br>\n")
    return f"<p>{html}</p>"


def send_digest(subject: str, markdown_content: str) -> bool:
    """
    يرسل المحتوى (Markdown) كرسالة بريد.
    المتغيرات: EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT.
    """
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    recipient = os.getenv("EMAIL_RECIPIENT")

    if not all([sender, password, recipient]):
        print("تحذير: لم يتم تعيين EMAIL_SENDER أو EMAIL_PASSWORD أو EMAIL_RECIPIENT — تخطي الإرسال.")
        return False

    try:
        html_content = _markdown_to_html(markdown_content)
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject

        body = f"""
        <html>
          <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 700px;">
            <div style="background-color: #f4f4f4; padding: 20px;">
              <div style="background-color: white; padding: 24px; border-radius: 8px;">
                {html_content}
              </div>
              <p style="font-size: 12px; color: #888; margin-top: 20px;">
                Daily Brief — New_ara
              </p>
            </div>
          </body>
        </html>
        """
        msg.attach(MIMEText(body, "html"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()

        print("تم إرسال البريد بنجاح إلى:", recipient)
        return True
    except Exception as e:
        print("فشل إرسال البريد:", e)
        return False
