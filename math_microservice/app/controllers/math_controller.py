from flask import Blueprint, request, jsonify
from app.services import math_service
from app.logger import logger
from app.models import MathRequest
from app.db import db
from app.auth import require_auth, get_current_user
from app.schemas import PowRequest, FactorialRequest, FibonacciRequest, MathResponse

import json

math_bp = Blueprint('math', __name__)

@math_bp.route('/pow', methods=['POST'])
@require_auth
def pow_route():
    """
    Calculează ridicarea la putere a unui număr.
    ---
    tags:
      - Math
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - base
            - exp
          properties:
            base:
              type: integer
              example: 2
            exp:
              type: integer
              example: 8
    responses:
      200:
        description: Rezultatul operației pow
        schema:
          type: object
          properties:
            result:
              type: integer
              example: 256
            operation:
              type: string
              example: pow
            user:
              type: string
              example: alice@endava.com
      401:
        description: Token lipsă sau invalid
      400:
        description: Eroare de validare sau server
    security:
      - Bearer: []
    """
    try:
        data = request.get_json()
        req = PowRequest(**data)
        user = get_current_user()
        result = math_service.pow_op(req.base, req.exp)
        math_req = MathRequest(
            operation="pow",
            input_data=json.dumps(data),
            result=str(result),
            user=user
        )
        db.session.add(math_req)
        db.session.commit()
        logger.log(f"[{user}] POW: {req.base} ** {req.exp} = {result}", f"POW|{user}|{req.base}|{req.exp}|{result}")
        return jsonify(MathResponse(result=result, operation="pow", user=user).dict())
    except Exception as e:
        logger.log(f"Error in pow_route: {str(e)}")
        return jsonify({"error": str(e)}), 400

@math_bp.route('/factorial', methods=['POST'])
@require_auth
def factorial_route():
    """
    Calculează factorialul unui număr.
    ---
    tags:
      - Math
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - n
          properties:
            n:
              type: integer
              example: 5
    responses:
      200:
        description: Rezultatul operației factorial
        schema:
          type: object
          properties:
            result:
              type: integer
              example: 120
            operation:
              type: string
              example: factorial
            user:
              type: string
              example: alice@endava.com
      401:
        description: Token lipsă sau invalid
      400:
        description: Eroare de validare sau server
    security:
      - Bearer: []
    """
    try:
        data = request.get_json()
        req = FactorialRequest(**data)
        user = get_current_user()
        result = math_service.factorial_op(req.n)
        math_req = MathRequest(
            operation="factorial",
            input_data=json.dumps(data),
            result=str(result),
            user=user
        )
        db.session.add(math_req)
        db.session.commit()
        logger.log(f"[{user}] FACTORIAL: {req.n}! = {result}", f"FACTORIAL|{user}|{req.n}|{result}")
        return jsonify(MathResponse(result=result, operation="factorial", user=user).dict())
    except Exception as e:
        logger.log(f"Error in factorial_route: {str(e)}")
        return jsonify({"error": str(e)}), 400

@math_bp.route('/fibonacci', methods=['POST'])
@require_auth
def fibonacci_route():
    """
    Calculează al n-lea număr Fibonacci.
    ---
    tags:
      - Math
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - n
          properties:
            n:
              type: integer
              example: 7
    responses:
      200:
        description: Rezultatul operației fibonacci
        schema:
          type: object
          properties:
            result:
              type: integer
              example: 13
            operation:
              type: string
              example: fibonacci
            user:
              type: string
              example: alice@endava.com
      401:
        description: Token lipsă sau invalid
      400:
        description: Eroare de validare sau server
    security:
      - Bearer: []
    """
    try:
        data = request.get_json()
        req = FibonacciRequest(**data)
        user = get_current_user()
        result = math_service.fibonacci_op(req.n)
        math_req = MathRequest(
            operation="fibonacci",
            input_data=json.dumps(data),
            result=str(result),
            user=user
        )
        db.session.add(math_req)
        db.session.commit()
        logger.log(f"[{user}] FIBONACCI: F({req.n}) = {result}", f"FIBONACCI|{user}|{req.n}|{result}")
        return jsonify(MathResponse(result=result, operation="fibonacci", user=user).dict())
    except Exception as e:
        logger.log(f"Error in fibonacci_route: {str(e)}")
        return jsonify({"error": str(e)}), 400

@math_bp.route('/history', methods=['GET'])
@require_auth
def history_route():
    """
    Returnează istoricul operațiilor matematice efectuate de utilizatorul curent.
    ---
    tags:
      - Math
    responses:
      200:
        description: Listă cu ultimele 100 de operații
        schema:
          type: array
          items:
            type: object
            properties:
              operation:
                type: string
              input_data:
                type: string
              result:
                type: string
              timestamp:
                type: string
                example: "2025-08-08T09:24:00"
      401:
        description: Token lipsă sau invalid
    security:
      - Bearer: []
    """
    user = get_current_user()
    requests = MathRequest.query.filter_by(user=user).order_by(MathRequest.timestamp.desc()).limit(100).all()
    logs = [
        {
            "operation": r.operation,
            "input_data": r.input_data,
            "result": r.result,
            "timestamp": r.timestamp.isoformat(),
        } for r in requests
    ]
    return jsonify(logs)
