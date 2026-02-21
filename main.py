from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import List, Optional
import math

app = FastAPI(title="Blackrock Challenge API")


# --- SCHEMAS ---

class TransactionBase(BaseModel):
    date: str  # Kept as string to handle the specific format manually
    amount: float

    @field_validator('date')
    @classmethod
    def validate_date_format(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
            return v
        except ValueError:
            raise ValueError('Date must be in format YYYY-MM-DD HH:mm:ss')


class TransactionEnriched(TransactionBase):
    ceiling: float
    remanent: float


class ValidatorInput(BaseModel):
    wage: float
    transactions: List[TransactionEnriched]


class InvalidTransaction(TransactionEnriched):
    message: str


class ValidatorOutput(BaseModel):
    valid: List[TransactionEnriched]
    invalid: List[InvalidTransaction]


# --- ENDPOINTS ---

# 1. Transaction Builder
@app.post("/blackrock/challenge/v1/transactions:parse", response_model=List[TransactionEnriched])
async def parse_transactions(transactions: List[TransactionBase]):
    output = []
    for item in transactions:
        # Business Logic: Round up to the nearest 100 based on your example (250 -> 300)
        ceiling_val = float(math.ceil(item.amount / 100) * 100)
        remanent_val = float(round(ceiling_val - item.amount, 2))

        output.append({
            "date": item.date,
            "amount": item.amount,
            "ceiling": ceiling_val,
            "remanent": remanent_val
        })
    return output


# 2. Transaction Validator
@app.post("/blackrock/challenge/v1/transactions:validator", response_model=ValidatorOutput)
async def validate_transactions(data: ValidatorInput):
    valid_list = []
    invalid_list = []

    for tx in data.transactions:
        # Example Validation Logic based on your image
        if tx.amount < 0:
            invalid_list.append({
                **tx.model_dump(),
                "message": "Negative amounts are not allowed"
            })
        else:
            valid_list.append(tx)

    return {"valid": valid_list, "invalid": invalid_list}

