function processData(input) {
    
    const lines = input.trim().split("\n");

    const n = parseInt(lines[0].trim());
    
    const phoneBook = new Map();
    
    
    for (let i = 1; i <= n; i++) {
        const [name, phone] = lines[i].trim().split(" ");
        phoneBook.set(name, phone);
    }
    
    for (let i = n + 1; i < lines.length; i++) {
        const queryName = lines[i].trim();
        
        if (!queryName) continue;
        
        if (phoneBook.has(queryName)) {
            console.log(`${queryName}=${phoneBook.get(queryName)}`);
        } else {
            console.log("Not found");
        }
    }
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});