{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1ac10379-641c-49d6-a871-a319e2db5abd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<========================================>\n",
      "           TEXT ANALYSER\n",
      "<========================================>\n",
      "1. Load text file\n",
      "2. Display basic statistics\n",
      "3. Word frequency analysis\n",
      "4. Sentence analysis\n",
      "5. Character analysis\n",
      "6. Export results\n",
      "7. Exit\n",
      "<========================================>\n",
      "Current file: \n",
      "\n",
      "__________________________________________\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input action (1-7):  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "__________File selection__________\n",
      "\n",
      "Available text files:\n",
      " 1. whatever file 101\n",
      " 2. whatever file 202\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter file number (1-x) from list above:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<========================================>\n",
      "           TEXT ANALYSER\n",
      "<========================================>\n",
      "1. Load text file\n",
      "2. Display basic statistics\n",
      "3. Word frequency analysis\n",
      "4. Sentence analysis\n",
      "5. Character analysis\n",
      "6. Export results\n",
      "7. Exit\n",
      "<========================================>\n",
      "Current file: \n",
      "\n",
      "__________________________________________\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Input action (1-7):  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shutting down\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "\n",
    "\n",
    "def main_menu():                                            #Start menyn där man väljer vilken funktion man vill använda\n",
    "    loaded_file = ''\n",
    "    print('<========================================>')\n",
    "    print('           TEXT ANALYSER')\n",
    "    print('<========================================>')\n",
    "    print('1. Load text file')\n",
    "    print('2. Display basic statistics')\n",
    "    print('3. Word frequency analysis')\n",
    "    print('4. Sentence analysis')\n",
    "    print('5. Character analysis')\n",
    "    print('6. Export results')\n",
    "    print('7. Exit')\n",
    "    print('<========================================>')\n",
    "    print(f'Current file: {loaded_file}')\n",
    "    print()\n",
    "    print('__________________________________________')\n",
    "    choice = int(input('Input action (1-7): '))\n",
    "    if choice > 0 and choice < 8:\n",
    "        while choice < 8:\n",
    "            if choice == 1:\n",
    "                load_text_file()\n",
    "            elif choice == 2:\n",
    "                display_basic_statistics()\n",
    "            elif choice == 3:\n",
    "                word_frequency_analysis()\n",
    "            elif choice == 4:\n",
    "                sentence_analysis()\n",
    "            elif choice == 5:\n",
    "                character_analysis()\n",
    "            elif choice == 6:\n",
    "                export_results()\n",
    "            elif choice == 7:\n",
    "                print('Shutting down')\n",
    "            else:\n",
    "                print('please enter a number between 1-7')\n",
    "            break\n",
    "    \n",
    "    \n",
    "    \n",
    "def load_text_file():                                    #Funktionen för att välja vilken fil man vill söka igenom\n",
    "    print()\n",
    "    print('__________File selection__________')\n",
    "    print()\n",
    "    print('Available text files:')\n",
    "    print(' 1. whatever file 101')\n",
    "    print(' 2. whatever file 202')\n",
    "    choice = input('Enter file number (1-x) from list above: ')\n",
    "    if choice == 1:\n",
    "        load_file1()\n",
    "    elif choice == 2:\n",
    "        load_file2()\n",
    "    else:\n",
    "        main_menu()\n",
    "\n",
    "#def display_basic_statistics()\n",
    "\n",
    "\n",
    "#def word_frequency_analysis()\n",
    "\n",
    "\n",
    "#def sentence_analysis()\n",
    "\n",
    "\n",
    "#def character_analysis()\n",
    "\n",
    "\n",
    "#def export_results()\n",
    "\n",
    "\n",
    "#def load_file1():\n",
    " #   file = open()\n",
    "  #  for line in file:\n",
    "  #      do whatever\n",
    "   # file.close\n",
    "    \n",
    "    \n",
    "\n",
    "    \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def main():                                          #Funktionen som jhälper till att anropa rätt funktion vid rätt tillfälle\n",
    "    main_menu()\n",
    "   \n",
    "\n",
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65ba4b59-9c6d-4ec5-a0f8-238b51ffcfe7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2740e88-9f94-4401-bc12-3c782fe78f56",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}