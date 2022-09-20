#!/usr/bin/python
# This script adds additional columns and populates the g2pconnect csv with MOSIP compatible data.
# Usage: python enhance_csv.py <original_csv> <output_csv>

import sys
import os
import argparse
import csv
from datetime import date
import random
import string

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('original_csv', help='Original CSV file', action='store')
    parser.add_argument('output_csv', help='Enhanced CSV file', action='store')
    args = parser.parse_args()
    return args, parser

def generate_random_token(): 
    token = ''.join(random.choices(string.digits[1:9], k=36))
    return token

def convert_date(d):
    d2 = date.fromisoformat(d)
    return d2.strftime('%Y/%m/%d') 
    
def main():
    args, parser = args_parse()
 
    print('Reading CSV')
    with open(args.original_csv, 'rt') as csvfile:
        reader = csv.DictReader(csvfile)
        # Add MOSIP specific fields
        fieldnames = reader.fieldnames + ['full_name', 'dob', 'email_id', 'full_address']
        output_rows = []
        for row in reader:
            row['full_name'] = row['given_name'] + ' ' + row['family_name']
            row['email_id'] = row['given_name'].lower() + row['family_name'].lower() + '@zmail.com'
            row['dob'] = convert_date(row['birthdate']) 
            row['full_address'] = ''
            if len(row['reg_ids/value'].strip()) == 0:
                row['reg_ids/value'] = generate_random_token()
            output_rows.append(row) 

    print('Writing output CSV')
    with open(args.output_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator=os.linesep) # Remove control-m chars
        writer.writeheader()
        writer.writerows(output_rows)
 
if __name__== '__main__':
    main()
       
