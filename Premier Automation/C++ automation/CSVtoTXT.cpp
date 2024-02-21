#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include "classCodesMap.h"
#include "input.h"


using namespace::std;

void createTxtFile(const string& cleanedFileName, const string& txtFileName);
void cleanAndExportCSV(const string& inputFileName, const string& outputFileName);
string inputCSV;
string cleanedCSV;
string txtFileName;
string response;


int main() {

    input("What is the path of your Input CSV file?", inputCSV);
    // Process the CSV file and export cleaned CSV
    cleanedCSV = inputCSV + "cleaned.csv";
    cleanAndExportCSV(inputCSV, cleanedCSV);

    // Create .txt file using cleaned CSV
    txtFileName = "output.txt";
    createTxtFile(cleanedCSV, txtFileName);

    return 0;
}

void cleanAndExportCSV(const string& inFile, const string& outFile) {
    ifstream infile(inFile);
    ofstream outfile(outFile);

 // Check if file is opened successfully
    if (!infile.is_open() || !outfile.is_open()) {
        cerr << "Error opening file!" << endl;
        return;
    }

    string line;
    while (getline(infile, line)) {
        // Process each line
        stringstream ss(line);
        string token;

        // Tokenize the line
        vector<string> tokens;
        while (getline(ss, token, ',')) {
            tokens.push_back(token);
        }

        string classCode1, classCode2, classCode3;

        // Iterate over specific indices (1, 2, 3)
        for (int i = 1; i <= 3 && i < tokens.size(); ++i) {
            // Check if the current index has a string containing a class code
            if (!tokens[i].empty()) {
                string classCode;
                // Extract class code from the token
                for (char c : tokens[i]) {
                    if (isdigit(c)) { // Include digits
                        classCode += c;
                    }
                }

                // Store class code in respective variables based on index
                if (i == 1) {
                    classCode1 = classCode;
                } else if (i == 2) {
                    classCode2 = classCode;
                } else if (i == 3) {
                    classCode3 = classCode;
                }
                // Search for the class code in the classMap
                auto it = classMap.find(classCode);
                if (it != classMap.end()) {
                    // Replace class code with class name
                    tokens[i] = it -> second;
                }
            }
        }

        // Reconstruct the line
        string cleanedLine;
        for (const string& t : tokens) {
            cleanedLine += t + ",";
        }
        cleanedLine.pop_back(); // Remove the last comma

        // Write the cleaned line to output CSV
        outfile << cleanedLine << endl;
    }

    infile.close();
    outfile.close();
}


// Function to create a .txt file using the cleaned CSV
void createTxtFile(const string& cleanedFileName, const string& txtFileName) {
    // Implementation to create .txt file using the cleaned CSV

}