const ts = require("typescript");
const parseArgs = require("minimist");
const process = require("process");

const args = parseArgs(process.argv.slice(2));
const file = args.f || args.file;

// parse file name from file path
const fileName = file.split("/").pop();

// read file
const src = ts.sys.readFile(file);

const node = ts.createSourceFile(fileName, src, ts.ScriptTarget.Latest);

process.stdout.write(JSON.stringify(node));
