# from fastapi import FastAPI, File, UploadFile, Form
# from fastapi.responses import JSONResponse
import shutil
import os
# vet ej hur datan från alla scopes & resultat ser ut men enkelt att ändra kan göra for-loop istället liks
# app = FastAPI()

cc_methods = {
    'dac': {'name': 'Direct Air Capture', 'cost_per_ton': 500}, # teoretisk data just nu kan vara nice att utöka med kostnadsdata från nätet
    'biochar': {'name': 'Biochar', 'cost_per_ton': 100},
    'reforestation': {'name': 'Reforestation', 'cost_per_ton': 50}
}

def get_results(data):
    dac = calculate_net_zero_cost(data, cc_methods['dac'])
    biochar = calculate_net_zero_cost(data, cc_methods['biochar'])
    reforestation = calculate_net_zero_cost(data, cc_methods['reforestation'])
    result_string = (
        f"You selected the method: {dac['method']}, "
        f"with Scope 1: {dac['scope1']} tCO₂e, "
        f"Scope 2: {dac['scope2']} tCO₂e, and "
        f"Scope 3: {dac['scope3']} tCO₂e. "
        f"Total emissions: {dac['total_emissions']} tCO₂e. "
        f"The cost to offset these emissions is {dac['cost_to_offset']} SEK, "
        f"which is {dac['percentage_of_revenue']}% of your revenue."
    )

    return result_string



def extract_emissions_from_pdf(file_path):
    return {
        "scope1": 12000,
        "scope2": 8000,
        "scope3": 15000,
        "revenue": 5_000_000
    }

def calculate_net_zero_cost(data, cc_method):
    scope1 = data.get("scope1", 0)
    scope2 = data.get("scope2", 0)
    scope3 = data.get("scope3", 0)
    revenue = data.get("profit")

    total_emissions = scope1 + scope2 + scope3
    cost_to_offset = total_emissions * cc_method['cost_per_ton']
    percentage = (cost_to_offset / revenue) * 100

    return {
        "method": cc_method["name"],
        "scope1": scope1,
        "scope2": scope2,
        "scope3": scope3,
        "total_emissions": total_emissions,
        "cost_to_offset": round(cost_to_offset, 2),
        "percentage_of_revenue": round(percentage, 2)
        
    }

# @app.post("/upload")
# async def upload_pdf(file: UploadFile = File(...), method: str = Form(...)):
#     temp_path = f"temp_{file.filename}"
#     with open(temp_path, "wb") as f:
#         shutil.copyfileobj(file.file, f)

#     try:
#         extracted_data = extract_emissions_from_pdf(temp_path)
#         selected_method = cc_methods.get(method)

#         if not selected_method:
#             return JSONResponse(status_code=400, content={"error": "Invalid method"})

#         result = calculate_net_zero_cost(extracted_data, selected_method)
#         return JSONResponse(content=result)
#     finally:
#         os.remove(temp_path)
