from pydantic import BaseModel, Field 
from typing import Literal , Annotated


class UserInput(BaseModel):
    gender: Annotated[Literal['Female', 'Male'], Field(...,description="Gender of the customer")]
    SeniorCitizen: Annotated[Literal[0, 1], Field(...,description="Whether the customer is a senior citizen (1) or not (0)")]
    Partner: Annotated[Literal['Yes', 'No'], Field(...,description="Whether the customer has a partner")]
    Dependents: Annotated[Literal['Yes', 'No'], Field(title="Whether the customer has dependents")]
    tenure: Annotated[int, Field(...,description="Number of months the customer has stayed with the company", ge=0)]
    PhoneService: Annotated[Literal['Yes', 'No'], Field(...,description="Whether the customer has phone service")]
    MultipleLines: Annotated[Literal['Yes', 'No', 'No phone service'], Field(...,description="Whether the customer has multiple lines")]
    InternetService: Annotated[Literal['DSL', 'Fiber optic', 'No'], Field(...,description="Type of internet service")]
    OnlineSecurity: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...,description="Whether the customer has online security")]
    OnlineBackup: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...,description="Whether the customer has online backup")]
    DeviceProtection: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...,description="Whether the customer has device protection")]
    TechSupport: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...,description="Whether the customer has tech support")]
    StreamingTV: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...,description="Whether the customer streams TV")]
    StreamingMovies: Annotated[Literal['Yes', 'No', 'No internet service'], Field(...,description="Whether the customer streams movies")]
    Contract: Annotated[Literal['Month-to-month', 'One year', 'Two year'], Field(...,description="Type of contract")]
    PaperlessBilling: Annotated[Literal['Yes', 'No'], Field(...,description="Whether the customer has paperless billing")]
    PaymentMethod: Annotated[Literal['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], Field(title="Payment method used by the customer")]
    MonthlyCharges: Annotated[float, Field(...,description="The amount charged to the customer monthly", ge=0)]
    TotalCharges: Annotated[float, Field(...,description="The total amount charged to the customer", ge=0)]
    

