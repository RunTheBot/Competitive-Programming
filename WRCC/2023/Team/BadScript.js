const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];

function ifReplacer(match) {
    let condition = match.replace("if", "").replace(":", "");
    return `if (${condition}) {`

}

function repeatReplacer(match) {
    // console.log(match);
    let condition = match.replace("repeat", "").replace(":", "");
    // console.log(condition);
    return `for (let i = 0; i < ${condition}; i++) {`

}

const start = async () => {
    firstLine = await rl[Symbol.asyncIterator]().next();
    firstLine = firstLine.value.split(" ")
    let xVal = parseInt(firstLine[0]);
    let n = parseInt(firstLine[1]);
    
    for await (const line of rl) {
        lines.push(line);
        if (lines.length === n) {
            rl.close();
            break;
        }
    }
    let unparsedCode = lines.join("\n");
    
    let code = unparsedCode
        .replace(/end.*?;/g, "}")
        .replace(/if.*?:/g, ifReplacer)
        .replace(/repeat.*?:/g, repeatReplacer)

    // console.log(`\n\nlet x = ${xVal};\n${code}\nconsole.log(x);\n\n\n`);
    
    eval(`let x = ${xVal};\n${code}\nprocess.stdout.write(x.toString());`);
    
}
start();