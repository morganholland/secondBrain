# Enhanced Writing Bot - Based on Classic Writing Guides

A Python-based writing bot that analyzes and improves text based on proven writing principles from multiple authoritative sources.

## Key Writing Rules Applied

The bot analyzes text against writing principles from:

### Wes Kao's Principles (from Lenny's Podcast):
1. **Super Specific "How"** - Focus on actionable implementation details rather than just "what" and "why"
2. **Start Right Before You Get Eaten by the Bear** - Cut unnecessary backstory and get to the point immediately  
3. **Eyes Light Up Principle** - Focus on genuinely engaging content that creates real reader engagement
4. **Avoid Communication Surprises** - Be clear about recommendations and don't hide your point of view
5. **Over-communicate** - Err on the side of providing adequate context rather than leaving gaps

### Classic Writing Guides Integration:
6. **Bottom Line Up Front** - Lead with conclusions, then provide supporting context (Minto Pyramid Principle)
7. **Sentence Structure** - Use clear, concise sentences with proper structure (June Casagrande principles)
8. **Active Voice** - Prefer active voice over passive voice for clarity and directness (Business Writing)
9. **Logical Flow** - Structure arguments logically with clear hierarchy (Minto Pyramid)
10. **Conciseness** - Eliminate unnecessary words and redundant phrases (All guides)
11. **Clarity & Simplicity** - Write clearly and simply, avoid jargon (William Zinsser)
12. **Eliminate Clutter** - Remove unnecessary words, adverbs, and complexity (Zinsser)

## Usage

### Basic Usage
```bash
python writing_bot.py "Your text to analyze here"
```

### From File
```bash
python writing_bot.py --file your_document.txt
```

### From Stdin
```bash
python writing_bot.py
# Then paste your text and press Ctrl+D when done
```

### Save Results
```bash
python writing_bot.py --file input.txt --output results.txt
```

## How It Works

The bot analyzes your text against each writing principle and provides:

- **Pass/Fail Status** for each principle
- **Specific Issues** found in your text
- **Actionable Suggestions** for improvement
- **Explanation** of why each rule matters

## Example Output

```
WRITING ANALYSIS BASED ON WES KAO'S PRINCIPLES
============================================================

Super Specific How: ✗ ISSUES FOUND
  Focus on actionable 'how' rather than 'what' and 'why'
  Issues:
    • Potential vague advice without specific implementation: 'you should be'
    • Text lacks specific implementation details - consider adding 'how-to' elements

Bottom Line First: ✗ ISSUES FOUND  
  Lead with conclusions, then provide context
  Issues:
    • Main conclusion or recommendation may be buried - consider leading with the key takeaway

SUGGESTIONS FOR IMPROVEMENT:
  • Add specific steps, examples, or concrete implementation details
  • Start with: 'Bottom line: [your main point]'
```

## Installation

No external dependencies required - uses only Python standard library.

```bash
python writing_bot.py
```

## Writing Principles Explained

### 1. Super Specific How
Replace vague advice like "you should communicate better" with specific steps like "Here's how to structure your emails: 1) Bottom line first, 2) Context second, 3) Action items last."

### 2. Cut Backstory  
Instead of "Let me give you some background on this topic and then explain the concept...", start with "The key insight is that most people manage their boss wrong. Here's the better way..."

### 3. Clear Recommendations
If presenting options, clearly state which you recommend: "I recommend Option A because [specific reasons]. Here are the trade-offs..."

### 4. Bottom Line First
Structure: "Bottom line: [your main point]. Here's why: [supporting context]."

### 5. Adequate Context
Provide enough context for readers to understand without overwhelming them with unnecessary details.

### 6. Clarity & Simplicity (Zinsser)
Replace jargon with simple words: "utilize" → "use", "facilitate" → "help", "leverage" → "use"

### 7. Eliminate Clutter (Zinsser)
Remove unnecessary qualifiers: "very good" → "excellent", "really important" → "crucial"

## Enhanced Features

The bot now includes analysis based on four classic writing guides:

- **June Casagrande's "It Was the Best of Sentences"** - Focuses on sentence structure, clarity, and eliminating weak constructions
- **Barbara Minto's "Pyramid Principle"** - Emphasizes logical structure, bottom-line-first communication, and clear argument flow  
- **HBR Guide to Better Business Writing** - Covers active voice, conciseness, and professional communication standards
- **William Zinsser's "On Writing Well"** - Emphasizes clarity, simplicity, and eliminating clutter words

## Example Enhanced Analysis

The bot now detects and suggests improvements for:
- **Sentence Structure**: Long sentences, weak openings, unclear pronouns (Casagrande)
- **Active vs Passive Voice**: Identifies passive constructions and suggests active alternatives (HBR)
- **Logical Flow**: Checks for proper transitions, topic sentences, and hierarchical organization (Minto)
- **Conciseness**: Finds redundant phrases and suggests shorter, clearer alternatives (HBR)
- **Clarity & Simplicity**: Detects jargon and suggests simpler alternatives (Zinsser)
- **Eliminate Clutter**: Identifies unnecessary qualifiers and weak word combinations (Zinsser)

---

*Built based on insights from Wes Kao's interview on Lenny's Podcast combined with proven principles from classic writing guides including Casagrande, Minto, HBR, and Zinsser.*
# Last updated: Wed Oct 15 17:32:36 EDT 2025
