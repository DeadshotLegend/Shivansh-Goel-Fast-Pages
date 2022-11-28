---
toc: true
layout: post
description: PBL BInary File
categories: [markdown, Week 13]
title: PBL Binary File
---

<head>
	<title>Hacks</title>
</head>
<div class="container">
	<h1>Hack #1</h1>
	<p>Decimal: <span id="decimal"></span></p>
	<p>Hexadecimal: <span id="hex"></span></p>
	<p>Octal: <span id="octal"></span></p>
	<p id="error"></p>
	<p>Binary: <input id="number" /></p>
	<div id="bits"></div>

	<h1>Hack #2</h1>
	<p>Color code: rgb(<span id="colorCode"></span>)</p>
	<p>Hex: <span id="colorHex"></span></p>
	<div id="colorBox"></div>

	<h1>Hack #3</h1>
	<p id="baseError"></p>
	<p>Enter arbitrary base (2-36): <input id="base" /></p>
	<p>Base-<span id="baseValue">N</span> format: <span id="baseN"></span></p>

	<script>
		const BITS = 8;
		let isFocused = false;
		let isBinError = false;
		let isBaseError = false;

		const reactive = (init, cb) => {
			let value = init;

			const setValue = (i) => {
				if (typeof i === "function") {
					value = i(value);
				} else if (typeof i === "string") {
					value = i;
				}

				if (typeof cb === "function") {
					cb(value);
				} else if (Array.isArray(cb)) {
					cb.forEach((c) => c(value));
				}
			};

			const getValue = () => value;
			return [getValue, setValue];
		};

		const number = document.getElementById("number");
		const bitsContainer = document.getElementById("bits");
		const error = document.getElementById("error");
		const baseError = document.getElementById("baseError");
		const colorBox = document.getElementById("colorBox");

		const decimal = document.getElementById("decimal");
		const hex = document.getElementById("hex");
		const octal = document.getElementById("octal");
		const colorHex = document.getElementById("colorHex");
		const colorCode = document.getElementById("colorCode");
		const baseEl = document.getElementById("base");
		const baseValue = document.getElementById("baseValue");
		const baseN = document.getElementById("baseN");

		bitsContainer.style.gridTemplateColumns = `repeat(${BITS}, 1fr)`;

		const setNumberHTML = (v) => {
			number.value = v;
		};

		const setBits = (v) => {
			if (!/^[0|1]*$/.test(v)) {
				error.innerHTML = "error: invalid input: input must consist of only 1s and 0s";
				isBinError = true;
				return;
			} else {
				error.innerHTML = "";
				isBaseError = false;
			}

			const num = Number.parseInt(v, 2);
			const max = Math.pow(2, BITS);
			if (num > max) {
				error.innerHTML = `error: invalid input: number ${num} is too large (max: ${max})`;
				return;
			} else {
				isBaseError = false;
			}

			for (let b = 0; b < BITS; b++) {
				const place = Math.pow(2, b);
				const el = document.getElementById(`bit-${b}`).firstChild;
				if ((num & place) === place) {
					el.innerHTML = "1";
				} else {
					el.innerHTML = "0";
				}
			}
		};

		const setColor = (v) => {
			if (v === "" || isBinError) return;
			const val = Number.parseInt(v, 2);
			colorBox.style.backgroundColor = `rgb(${val}, ${val}, ${val})`;
		};

		const updateFormats = (v) => {
			if (v === "" || isBinError) return;
			const val = Number.parseInt(v, 2);
			decimal.innerHTML = val.toString(10);
			hex.innerHTML = val.toString(16).padStart(2, "0");
			octal.innerHTML = val.toString(8);
			colorCode.innerHTML = `${val}, ${val}, ${val}`;
			colorHex.innerHTML = `#${hex.innerHTML}${hex.innerHTML}${hex.innerHTML}`;
		};

		const [value, setValue] = reactive("", [setNumberHTML, setBits, setColor, updateFormats]);

		const setBaseHTML = (b) => {
			if (isBinError) return;
			baseValue.innerHTML = b;
		};

		const setBaseN = (b) => {
			if (b === "" || value() === "") return;
			const baseNValue = Number.parseInt(b);
			if (baseNValue < 2 || baseNValue > 36) {
				baseError.innerHTML = "error: invalid input: must be between 2 and 36";
				isBinError = true;
				return;
			} else {
				baseError.innerHTML = "";
				isBinError = false;
			}

			baseN.innerHTML = Number.parseInt(value(), 2).toString(baseNValue);
		};

		const [base, setBase] = reactive("", [setBaseHTML, setBaseN]);

		for (let i = 0; i < BITS; i++) {
			const bitFlip = document.createElement("div");
			const bitValue = document.createElement("p");
			const flipBtn = document.createElement("button");

			const bitId = BITS - i - 1;
			bitFlip.id = `bit-${bitId}`;
			bitFlip.classList.add("bitFlip");
			bitValue.innerHTML = "0";
			flipBtn.innerHTML = "Flip";

			flipBtn.addEventListener("click", () => {
				const currentBit = Number.parseInt(bitValue.innerHTML);
				const flipped = currentBit === 0 ? 1 : 0;

				setValue((prev) => {
					const numeric = Number.parseInt(prev, 2);
					const newValue = numeric ^ Math.pow(2, bitId);
					return newValue.toString(2).padStart(BITS, "0");
				});
			});

			bitFlip.appendChild(bitValue);
			bitFlip.appendChild(flipBtn);
			bitsContainer.appendChild(bitFlip);
		}

		number.addEventListener("input", () => {
			setValue(number.value);
		});

		baseEl.addEventListener("input", () => {
			setBase(baseEl.value);
		});
	</script>

	<style>
		#bits {
			max-width: 600px;
			display: grid;
			gap: 1rem;
			margin-top: 1rem;
		}

		.bitFlip {
			padding: 0.5rem;
			display: flex;
			flex-direction: column;
			align-items: center;
		}

		#error,
		#baseError {
			color: red;
		}

		h1 {
			font-weight: bold;
			font-size: 2rem;
		}

		#colorBox {
			margin-top: 0.5rem;
			width: 100px;
			height: 100px;
		}

		.bitFlip,
		input {
			outline: none !important;
			border: 1px solid black;
			border-radius: 5px;
		}

		button {
			outline: none;
			border: none;
			background-color: #ff5e5e !important;
			color: white !important;
			border-radius: 5px;
		}

		button:hover {
			background-color: rgb(182, 57, 57) !important;
		}

		p {
			margin: 0rem 0rem !important;
		}
	</style>
</div>