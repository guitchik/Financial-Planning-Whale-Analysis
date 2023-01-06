{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "818d493f-d151-4c13-b786-bc24679c9032",
   "metadata": {},
   "outputs": [],
   "source": [
    "#imports\n",
    "from pathlib import Path\n",
    "import csv\n",
    "\n",
    "#global variables\n",
    "csvpath = Path('Resources/budget_data.csv')\n",
    "\n",
    "total_months = 0 #int\n",
    "total = 0 #int\n",
    "average_change_sum = 0 #int\n",
    "dict = {} #dictionary\n",
    "\n",
    "\n",
    "with open (csvpath, 'r') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter =  ',')\n",
    "    \n",
    "    csvheader = next(csvreader)\n",
    "    previous_month_pl = 0\n",
    "    \n",
    "    for row in csvreader:\n",
    "        total_months += 1\n",
    "        current_month_pl = int(row[1])\n",
    "        total += current_month_pl\n",
    "        date = row[0]\n",
    "        monthly_change = 0\n",
    "        \n",
    "        if previous_month_pl:\n",
    "            monthly_change = current_month_pl - previous_month_pl\n",
    "            average_change_sum += monthly_change\n",
    "            \n",
    "        previous_month_pl = current_month_pl\n",
    "        \n",
    "        dict[date] = monthly_change\n",
    "\n",
    "        \n",
    "    average_change = round(average_change_sum / (total_months - 1), 2)\n",
    "    max_increase = max(dict, key = dict.get)\n",
    "    min_increase = min(dict, key = dict.get)\n",
    "    \n",
    "with open('output.txt', 'w') as file:\n",
    "    # @TODO: Write daily_average to the output file, convert to string\n",
    "    file.write(f'Financial Analysis\\n')\n",
    "    file.write(f'-----------------------------\\n')\n",
    "    file.write(f'Total Months:  {total_months}\\n')\n",
    "    file.write(f'Total:  {total}\\n')\n",
    "    file.write(f'Greatest Increase in Profits:  {max_increase} ${dict[max_increase]}\\n')\n",
    "    file.write(f'Greatest Decrease in Profits:  {min_increase} (${dict[min_increase]})\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24e07e20-07a6-46de-a884-eb04b497de57",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16df3b51-50b8-48ec-a692-caca5357ebda",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
