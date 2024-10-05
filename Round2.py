collections = {}

def createCollection(p_collection_name):
    if p_collection_name not in collections:
        collections[p_collection_name] = []
        print(f"Collection '{p_collection_name}' created successfully.")
    else:
        print(f"Collection '{p_collection_name}' already exists.")

def indexData(p_collection_name, p_exclude_column):
    if p_collection_name in collections:
        for record in collections[p_collection_name]:
            if p_exclude_column in record:
                del record[p_exclude_column]
        print(f"Indexed data in collection '{p_collection_name}', excluding column '{p_exclude_column}'.")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")

def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name in collections:
        results = [record for record in collections[p_collection_name] if record.get(p_column_name) == p_column_value]
        print(f"Search results for column '{p_column_name}' with value '{p_column_value}' in collection '{p_collection_name}':")
        return results
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
        return []

def getEmpCount(p_collection_name):
    if p_collection_name in collections:
        emp_count = len(collections[p_collection_name])
        print(f"Employee count in collection '{p_collection_name}': {emp_count}")
        return emp_count
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
        return 0

def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name in collections:
        initial_count = len(collections[p_collection_name])
        collections[p_collection_name] = [record for record in collections[p_collection_name] if record.get("employee_id") != p_employee_id]
        if len(collections[p_collection_name]) < initial_count:
            print(f"Employee with ID '{p_employee_id}' deleted from collection '{p_collection_name}'.")
        else:
            print(f"No employee with ID '{p_employee_id}' found in collection '{p_collection_name}'.")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")

def getDepFacet(p_collection_name):
    if p_collection_name in collections:
        department_count = {}
        for record in collections[p_collection_name]:
            department = record.get("department", "Unknown")
            if department in department_count:
                department_count[department] += 1
            else:
                department_count[department] = 1
        print(f"Employee count grouped by department in collection '{p_collection_name}': {department_count}")
        return department_count
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
        return {}


createCollection("employee_collection")

collections["employee_collection"] = [
    {"employee_id": 1, "name": "Icebear", "department": "Analytics", "age": 22},
    {"employee_id": 2, "name": "PanPan", "department": "Developing", "age": 22},
    {"employee_id": 3, "name": "Grizzy", "department": "Developing", "age": 23}
]

indexData("employee_collection", "age")

search_results = searchByColumn("employee_collection", "department", "Analytics")
print(search_results)

getEmpCount("employee_collection")

delEmpById("employee_collection", 3)

getDepFacet("employee_collection")
