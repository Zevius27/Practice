
import { practice } from "../practice/practice";


///////////////////////////////////////////////////////////////////////////
// Function calls will work Immediate Even if they aren't Connected
// [Problem : Multi page Unexpected Behaviour]
//////////////////////////////////////////////////////////////////


// Function calls are working + 1 Dir all check.


export function Test1MultiPageProblem() {
    // Create the element
    const newDiv = document.createElement('div');

    // Add content and attributes
    newDiv.textContent = 'Hello From MainTest!';

    // Add to the DOM
    document.body.appendChild(newDiv);

    // Test 
    console.log(" MainTest ");
}




// Test1MultiPageProblem()
// Function calls are working all check.
// mainTest()
// Updating speed check All working.