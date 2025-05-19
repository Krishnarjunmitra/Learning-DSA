import fs from 'fs';
import path from 'path';
import chalk from 'chalk';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Clear the terminal screen (cross-platform, ES module compatible)
if (process.platform === 'win32') {
  execSync('cls', { stdio: 'inherit' });
} else {
  execSync('clear', { stdio: 'inherit' });
}

// Define paths
const dataFolder = path.join(__dirname, 'data');
const testFolder = path.join(__dirname, 'test cases');

// Helper function to check if a test file exists for a code file
function hasTestFile(codeFileName) {
  const baseName = path.parse(codeFileName).name;
  const files = fs.readdirSync(testFolder);
  return files.some(file => {
    const testBaseName = path.parse(file).name;
    return testBaseName === `${baseName} test` || testBaseName.endsWith(' test');
  });
}

// List all files in the data directory
console.log(chalk.cyan('='.repeat(50)));
console.log(chalk.yellow('📋 AVAILABLE PROBLEMS:'));
console.log(chalk.cyan('='.repeat(50)));

try {
  const files = fs.readdirSync(dataFolder);
  
  if (files.length === 0) {
    console.log(chalk.red('No problems found in the data directory.'));
  } else {
    // Group files by whether they have a number prefix or not
    const numberedProblems = [];
    const nonNumberedProblems = [];
    
    files.forEach(file => {
      const baseName = path.parse(file).name;
      const hasTest = hasTestFile(file);
      const status = hasTest ? chalk.green('✅') : chalk.red('❌');
      
      // Check if filename starts with a number pattern like "13. "
      if (/^\d+\./.test(baseName)) {
        numberedProblems.push({ file, baseName, hasTest, status });
      } else {
        nonNumberedProblems.push({ file, baseName, hasTest, status });
      }
    });
    
    // Sort numbered problems by their number
    numberedProblems.sort((a, b) => {
      const numA = parseInt(a.baseName.match(/^\d+/)[0]);
      const numB = parseInt(b.baseName.match(/^\d+/)[0]);
      return numA - numB;
    });
    
    // Sort non-numbered problems alphabetically
    nonNumberedProblems.sort((a, b) => a.baseName.localeCompare(b.baseName));
    
    // Print numbered problems
    if (numberedProblems.length > 0) {
      console.log(chalk.yellow('\n📌 Numbered Problems:'));
      numberedProblems.forEach(({ file, baseName, status }) => {
        const number = baseName.match(/^\d+/)[0];
        const name = baseName.replace(/^\d+\.\s*/, '');
        console.log(`${status} ${chalk.cyan(number)}: ${name} ${chalk.gray(`(Run with: npm run test -- ${number})`)}`);
      });
    }
    
    // Print non-numbered problems
    if (nonNumberedProblems.length > 0) {
      console.log(chalk.yellow('\n📌 Other Problems:'));
      nonNumberedProblems.forEach(({ file, baseName, status }) => {
        console.log(`${status} ${baseName} ${chalk.gray(`(Run with: npm run test -- "${baseName}")`)}`);
      });
    }
    
    // Count problems with and without tests
    const withTests = [...numberedProblems, ...nonNumberedProblems].filter(p => p.hasTest).length;
    const totalProblems = files.length;
    
    console.log(chalk.cyan('\n' + '-'.repeat(50)));
    console.log(chalk.yellow('📊 SUMMARY:'));
    console.log(`Total Problems: ${totalProblems}`);
    console.log(`Problems with Tests: ${chalk.green(withTests)}`);
    console.log(`Problems without Tests: ${chalk.red(totalProblems - withTests)}`);
    console.log(chalk.cyan('_'.repeat(50)));
  }
} catch (err) {
  console.error(chalk.red(`Error reading directory: ${err.message}`));
  console.error(chalk.yellow('Make sure the "data" and "test cases" directories exist.'));
}

console.log('\nTo run a test:');
console.log(chalk.green('npm run test -- <problem_identifier>'));
console.log('Where problem_identifier can be:');
console.log('  - A problem number (like "13")');
console.log('  - A filename without extension (like "stack")');
console.log('  - A full problem name (like "13. stack")\n');

// Note: If you encounter a warning about 'type': 'module' in package.json,
// ensure your package.json includes "type": "module" to use ES module syntax.