accepted_types = {
    'uksi': 'UK Statutory Instruments',
    'ukci': 'Church Instruments',
    'uksro': 'Statutory Rules and Orders',
    'ukpga': 'Public General Acts',
    'ukla': 'Local Acts',
    'ukcm': 'Church of England Measures',
}

uksi = [
    "Order",
    "Regulation",
    "Rule",
    "Scheme",
    "Direction",
    "Declaration",
]



def detect_type(_type,title):
    if _type == "uksi":
        return detect_uksi_type(title)
    elif _type in accepted_types.keys():
        return accepted_types[_type]
    else:
        return None

def detect_uksi_type(title:str):
    title = title.lower()
    title = title.replace("order of","",len(title))
    indices = []
    for uksi_ in uksi:
        indices.append(title.rfind(uksi_.lower()))
    max_ = indices.index(max(indices))
    if max(indices) == -1:
        return "نامشخص"
    return uksi[max_]

# print(detect_uksi_type("The Nursing and Midwifery Council (Fees) Rules Order of Council 2004"))