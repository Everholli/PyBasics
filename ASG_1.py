{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6b9e3e1a-2f14-4595-b957-b25f611f2039",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== Employee Management System =====\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- All Employees ---\n",
      "----------------------------------------------------------------------\n",
      "ID        Name           Age       Department     Salary         \n",
      "----------------------------------------------------------------------\n",
      "101       Satya          27        HR             50000.00       \n",
      "----------------------------------------------------------------------\n",
      "\n",
      "===== Employee Management System =====\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Add Employee ---\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Employee ID:  102\n",
      "Enter Employee Name:  Zaid\n",
      "Enter Employee Age:  22\n",
      "Enter Department:  IT\n",
      "Enter Monthly Salary:  500000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Employee added successfully!\n",
      "\n",
      "===== Employee Management System =====\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for using Employee Management System!\n"
     ]
    }
   ],
   "source": [
    "# Employee Management System\n",
    "\n",
    "employees = {\n",
    "    101: {\n",
    "        \"name\": \"Shruti\",\n",
    "        \"age\": 27,\n",
    "        \"department\": \"HR\",\n",
    "        \"salary\": 50000\n",
    "    }\n",
    "}\n",
    "\n",
    "\n",
    "def add_employee():\n",
    "    print(\"\\n--- Add Employee ---\")\n",
    "\n",
    "    emp_id = int(input(\"Enter Employee ID: \"))\n",
    "\n",
    "    while emp_id in employees:\n",
    "        print(\"Employee ID already exists!\")\n",
    "        emp_id = int(input(\"Enter a different Employee ID: \"))\n",
    "\n",
    "    name = input(\"Enter Employee Name: \")\n",
    "    age = int(input(\"Enter Employee Age: \"))\n",
    "    department = input(\"Enter Department: \")\n",
    "    salary = float(input(\"Enter Monthly Salary: \"))\n",
    "\n",
    "    employees[emp_id] = {\n",
    "        \"name\": name,\n",
    "        \"age\": age,\n",
    "        \"department\": department,\n",
    "        \"salary\": salary\n",
    "    }\n",
    "\n",
    "    print(\"Employee added successfully!\")\n",
    "\n",
    "\n",
    "def view_employees():\n",
    "    print(\"\\n--- All Employees ---\")\n",
    "\n",
    "    if not employees:\n",
    "        print(\"No employees available.\")\n",
    "        return\n",
    "\n",
    "    print(\"-\" * 70)\n",
    "    print(f\"{'ID':<10}{'Name':<15}{'Age':<10}{'Department':<15}{'Salary':<15}\")\n",
    "    print(\"-\" * 70)\n",
    "\n",
    "    for emp_id, details in employees.items():\n",
    "        print(\n",
    "            f\"{emp_id:<10}\"\n",
    "            f\"{details['name']:<15}\"\n",
    "            f\"{details['age']:<10}\"\n",
    "            f\"{details['department']:<15}\"\n",
    "            f\"{details['salary']:<15.2f}\"\n",
    "        )\n",
    "\n",
    "    print(\"-\" * 70)\n",
    "\n",
    "\n",
    "def search_employee():\n",
    "    print(\"\\n--- Search Employee ---\")\n",
    "\n",
    "    emp_id = int(input(\"Enter Employee ID: \"))\n",
    "\n",
    "    if emp_id in employees:\n",
    "        employee = employees[emp_id]\n",
    "\n",
    "        print(\"\\nEmployee Found!\")\n",
    "        print(\"Employee ID :\", emp_id)\n",
    "        print(\"Name        :\", employee[\"name\"])\n",
    "        print(\"Age         :\", employee[\"age\"])\n",
    "        print(\"Department  :\", employee[\"department\"])\n",
    "        print(\"Salary      :\", employee[\"salary\"])\n",
    "    else:\n",
    "        print(\"Employee not found.\")\n",
    "\n",
    "\n",
    "def main_menu():\n",
    "\n",
    "    while True:\n",
    "        print(\"\\n===== Employee Management System =====\")\n",
    "        print(\"1. Add Employee\")\n",
    "        print(\"2. View All Employees\")\n",
    "        print(\"3. Search for Employee\")\n",
    "        print(\"4. Exit\")\n",
    "\n",
    "        choice = input(\"Enter your choice: \")\n",
    "\n",
    "        if choice == \"1\":\n",
    "            add_employee()\n",
    "\n",
    "        elif choice == \"2\":\n",
    "            view_employees()\n",
    "\n",
    "        elif choice == \"3\":\n",
    "            search_employee()\n",
    "\n",
    "        elif choice == \"4\":\n",
    "            print(\"Thank you for using Employee Management System!\")\n",
    "            break\n",
    "\n",
    "        else:\n",
    "            print(\"Invalid choice. Please enter 1-4.\")\n",
    "\n",
    "\n",
    "main_menu()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6933d8d4-b4cd-4ff6-9966-8972b720e15a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
