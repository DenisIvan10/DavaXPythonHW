from datetime import datetime
from app.db import db

class MathRequest(db.Model):
    __tablename__ = 'math_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(50), nullable=False)  # 'pow', 'factorial', 'fibonacci'
    input_data = db.Column(db.String(100), nullable=False)  # serializăm inputul ca JSON/text
    result = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(100), nullable=False)  # pentru autorizare
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<MathRequest {self.operation} - {self.input_data} = {self.result}>"
