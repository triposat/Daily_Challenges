<p align="center">
  <img width="5%" src="https://user-images.githubusercontent.com/69134468/149906490-2fcac235-bc3e-4d4b-89a1-2cd3064bf1ef.png"/>
  <img width="14%" src="https://user-images.githubusercontent.com/69134468/139599658-8471e6db-f919-4606-899c-88d5b6e5d71a.png"/>
  <img width="5%" src="https://user-images.githubusercontent.com/69134468/149906490-2fcac235-bc3e-4d4b-89a1-2cd3064bf1ef.png"/>
</p>

## <h3>**Time Complexity:** </h3>
- [X] Follow the Rule: **10<sup>8</sup>** Operations 

<img align="right" src="https://github.com/Iamtripathisatyam/iamtripathisatyam/blob/master/Content/rock.gif" width="200"/>

| Length of Input (N) | Worst Accepted Algorithm |
| --------------  | ------------- |
| **≤ [10..11]**| **O(N!), O(N<sup>6</sup>)** |
| **≤ [15..18]** | **O(2<sup>N</sup> * N<sup>2</sup>)**  |
| **≤ [18..22]**  | **O(2<sup>N</sup> * N)** |
| **≤ 100**   | **O(N<sup>4</sup>)** |
| **≤ 400**   | **O(N<sup>3</sup>)** |
| **≤ 2000**   | **O(N<sup>2</sup> * logN)** |
| **≤ 10<sup>4</sup>**   | **O(N<sup>2</sup>)** |
| **≤ 10<sup>5</sup>**   |  **O(N * logN)** |
| **≤ 10<sup>6</sup>**   | **O(N)**, **O(logN)**, **O(1)** |

## <h3>**Basic Things 😁** </h3>
- If we have given any string let's say "abc":
  - Total Substring/Subarray: **n(n+1)/2**, here we have **6** (a, ab, abc, b, bc, c).
  - Total Subsequence/Subset: **2^n**, here we have **8** (_, a, b, c, ab, bc, ac, abc).
- How many operations can a CPU do?
  - It can do **1,000,000** operations per **1/1000th** of a second.
- Handshake Formula:
  ```
  handshake(n) = (n-1) + handshake(n-1)
               = (n-1) + (n-2) + handshake(n-2)
               = (n-1) + (n-2) + .... 1 + 0
               = n * (n - 1)/2 
  ```
 - Catalan Number:
 	- Recursive Formula: 
 	<img width="322" alt="final_cata-removebg-preview" src="https://user-images.githubusercontent.com/69134468/151302534-ac5928d1-8743-4562-8e37-9dd2fe216f56.png">
 
	- General Formula: 

		```
		(2n)! / ((n + 1)!n!)
		```
	  
 ## <h3>**Some Conversions:** </h3>

## <h4 align="center">`Hexadecimal` ---> `Decimal`</h4>
### <ol align="center">3B<sub>16</sub> = 3×16<sup>1</sup> + 11×16<sup>0</sup> = 48 + 11  = 5`<sub>10</sub> , here **B = 11**</ol>

### <ol align="center">E7A9<sub>16</sub> = 14×16<sup>3</sup> + 7×16<sup>2</sup> + 10×16<sup>1</sup> + 9×16<sup>0</sup> = 57344 + 1792 + 160 + 9 = 59305<sub>10</sub> , here **E = 14** & **A = 10**</ol>

### <ol align="center">0.8<sub>16</sub> = 0×16<sup>0</sup> + 8×16<sup>-1</sup> = 0 + 0.5  = 0.5<sub>10</sub></ol>

### <ol align="center">1F.01B<sub>16</sub> = 1×16<sup>1</sup> + 15×16<sup>0</sup> + 0×16<sup>-1</sup> + 1×16<sup>-2</sup> + 11×16<sup>-3</sup> = 31.0065918<sub>10</sub></ol>

## <h4 align="center">`Decimal` ---> `Hexadecimal`</h4>
### <ol>Conversion Steps: </ol>
   - Divide the number by 16.
   - Get the integer quotient for the next iteration.
   - Get the remainder for the hex digit.
   - Repeat the steps until the quotient is equal to 0.
	
### <ol>Example #1: </ol>
### <ol>7562<sub>10</sub><ol/>	
	
| Division by 16 | Quotient | Remainder | Hex |
| --------------  | ------------- | ------------- | --- |
| 7562 / 16 | 472 | 10 | A |
| 472 / 16  | 29  | 8  | 8 |
| 29 / 16   | 1   | 13 | D |
| 1 / 16    | 0   | 1  | 1 |

### <ol>So, 7562<sub>10</sub> = 1D8A<sub>16</sub><ol/>

### <ol>Example #2: </ol>
### <ol>35631<sub>10</sub><ol/>
	
| Division by 16 | Quotient | Remainder | Hex |
| --------------  | ------------- | ------------- | --- |
| 35631 / 16 | 2226 | 15 | F |
| 2226 / 16  | 139  | 2  | 2 |
| 139 / 16   | 8   | 11 | B |
| 8 / 16    | 0   | 8  | 8 |

#### <ol>So, 35631<sub>10</sub> =  8B2F<sub>16</sub><ol/>
	
<img width="600" alt="DSAA-removebg-preview" src="https://user-images.githubusercontent.com/69134468/151486974-7d84a750-dcd5-452a-b1fe-8e7c0609a747.png">
	
 - **Arrays:**
	- **Sudoku** and **chess boards** are 2D arrays.
	- Contacts on a cell phone.
	- Your viewing screen is also a multidimensional array of pixels.
	- 2D arrays (as matrices) are used in **image processing**.
- **Matrix:**
	- Matrices are used for making **seismic surveys**.
	- Used for plotting graphs, statistics, and surveys and also to do scientific studies and research in almost all different fields.
- **String:**
	- **Spam email detection**.
	- **Plagiarism detection**.
- **Linear Search:**
	- Finding a word in a lexicographically-unsorted physical dictionary book.
- **Binary Search:**
	- Finding Page Number in a Book, e.g., Target Page Number is 35, you open at Page No. 15, it’s less, you move ahead and open 43, it is greater, you again move backward.
- **Linked List:**
	- The Browser's Next and Previous Button (**Linked List of URLs**).
	- A Music Player that allows you to skip to the next or previous song (**Doubly Linked List**).
	- In the Ludo game, the turn was passed to each player in a circular manner (**Circular Linked List**).
- **Stack:**
	- **Undo**/**Redo** operation.
	- **Recursion** (Inbuilt Stack).
	- Used in IDEs to check for **proper parentheses matching**.
	- **Scratch card’s** earned after Google pay transaction.
- **Queue:**
	- Your browser deletes the history past one month.
	- If you delete a picture on your phone, it will be in the "recently deleted" folder, which says "the images will be deleted permanently after one week."Here, all the images are stored in the queue, so it's easier to pop them from the rear, based on the image deletion date.
	- Waiting list: During online registration, sometimes you'll be put on the waiting list, all the requests are stored in the queue.
- **Tree:**
	- **File system: Folders** and subfolders (N-ary tree).
	- **E-commerce websites** : Category -> Sub-categories -> Products.
	- **Auto-suggestion** when you google or **Autocomplete** feature in searching (**Trie**).
- **Graph:**
	- Uber, Ola cab booking: show me the nearest available cars (BFS)
	- Scheduling Problems (DFS).
	- While booking buses/flights, you get a list of available routes.
	- In Facebook, users are considered to be the vertices, and if they are friends, then there is an edge running between them. Facebook’s "friend suggestion" algorithm uses graph theory. Facebook is an example of an undirected graph.
