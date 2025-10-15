// Writing Bot Frontend - Client-side analysis based on the Python bot logic

class WritingBot {
    constructor() {
        this.rules = {
            "super_specific_how": {
                "description": "Focus on actionable 'how' rather than 'what' and 'why'",
                "check": this.checkSuperSpecificHow.bind(this),
                "suggest": this.suggestSuperSpecificHow.bind(this)
            },
            "cut_backstory": {
                "description": "Start right before you get eaten by the bear - cut unnecessary backstory",
                "check": this.checkBackstory.bind(this),
                "suggest": this.suggestCutBackstory.bind(this)
            },
            "clear_recommendations": {
                "description": "Avoid communication surprises - be clear about your point of view",
                "check": this.checkClearRecommendations.bind(this),
                "suggest": this.suggestClearRecommendations.bind(this)
            },
            "bottom_line_first": {
                "description": "Lead with conclusions, then provide context (Minto Pyramid Principle)",
                "check": this.checkBottomLineFirst.bind(this),
                "suggest": this.suggestBottomLineFirst.bind(this)
            },
            "sentence_structure": {
                "description": "Use clear, concise sentences with proper structure (Casagrande principles)",
                "check": this.checkSentenceStructure.bind(this),
                "suggest": this.suggestSentenceStructure.bind(this)
            },
            "active_voice": {
                "description": "Prefer active voice over passive voice for clarity and directness",
                "check": this.checkActiveVoice.bind(this),
                "suggest": this.suggestActiveVoice.bind(this)
            },
            "logical_flow": {
                "description": "Structure arguments logically with clear hierarchy (Minto Pyramid)",
                "check": this.checkLogicalFlow.bind(this),
                "suggest": this.suggestLogicalFlow.bind(this)
            },
            "conciseness": {
                "description": "Eliminate unnecessary words and redundant phrases",
                "check": this.checkConciseness.bind(this),
                "suggest": this.suggestConciseness.bind(this)
            },
            "clarity_simplicity": {
                "description": "Write clearly and simply - avoid jargon and complex constructions (Zinsser)",
                "check": this.checkClaritySimplicity.bind(this),
                "suggest": this.suggestClaritySimplicity.bind(this)
            },
            "eliminate_clutter": {
                "description": "Remove unnecessary words, adverbs, and complexity (Zinsser principles)",
                "check": this.checkEliminateClutter.bind(this),
                "suggest": this.suggestEliminateClutter.bind(this)
            }
        };
    }

    analyzeText(text) {
        if (!text.trim()) {
            return null;
        }

        const results = {
            originalText: text,
            analysis: {},
            suggestions: []
        };

        for (const [ruleName, rule] of Object.entries(this.rules)) {
            const issues = rule.check(text);
            results.analysis[ruleName] = {
                passed: issues.length === 0,
                issues: issues,
                description: rule.description
            };

            if (issues.length > 0) {
                const suggestions = rule.suggest(text, issues);
                results.suggestions.push(...suggestions);
            }
        }

        return results;
    }

    // Analysis Methods (simplified versions of the Python logic)
    checkSuperSpecificHow(text) {
        const issues = [];
        
        const vaguePatterns = [
            /\b(you should|it's important to|make sure to)\s+(be|have|do|get|use)\s+\w+/gi,
            /\b(focus on|prioritize|emphasize)\s+\w+\s+(more|better)/gi
        ];

        vaguePatterns.forEach(pattern => {
            if (pattern.test(text)) {
                issues.push("Potential vague advice without specific implementation");
            }
        });

        const specificIndicators = [
            /\b(here's how|this is how|step 1|first,|second,|then|next)/gi,
            /\b(specifically|exactly|precisely)/gi,
            /\b(example|instance|case study)/gi,
            /\d+\s+(minutes|hours|days|steps)/gi
        ];

        const hasSpecificContent = specificIndicators.some(pattern => pattern.test(text));
        
        if (!hasSpecificContent && text.split(' ').length > 100) {
            issues.push("Text lacks specific implementation details - consider adding 'how-to' elements");
        }

        return issues;
    }

    checkBackstory(text) {
        const issues = [];
        const sentences = text.split('.').filter(s => s.trim());
        
        const backstoryIndicators = [
            /\b(let me|i want to|first, let me|to begin with|in order to understand)/gi,
            /\b(context|background|history|overview|introduction)/gi,
            /\b(going to|about to|planning to|will be talking about)/gi
        ];
        
        const firstThird = sentences.slice(0, Math.floor(sentences.length / 3));
        
        for (const sentence of firstThird) {
            for (const pattern of backstoryIndicators) {
                if (pattern.test(sentence)) {
                    issues.push(`Potential backstory in opening: '${sentence.trim().substring(0, 50)}...'`);
                    return issues;
                }
            }
        }
        
        return issues;
    }

    checkClearRecommendations(text) {
        const issues = [];
        
        const unclearPatterns = [
            /\b(you might want to|it could be|perhaps|maybe|consider)/gi,
            /\b(on one hand|on the other hand)\b.*\b(on the other hand|however|but)\b/gi
        ];
        
        for (const pattern of unclearPatterns) {
            if (pattern.test(text)) {
                issues.push("Potentially unclear recommendation - consider stating your position more directly");
            }
        }

        if (/\b(pros?|advantages?)\b.*\b(cons?|disadvantages?)\b/gi.test(text) && 
            !/\b(recommend|suggest|think|believe)\b/gi.test(text)) {
            issues.push("Pros/cons list detected without clear recommendation - state your position upfront");
        }
        
        return issues;
    }

    checkBottomLineFirst(text) {
        const issues = [];
        const sentences = text.split('.').filter(s => s.trim());
        
        if (sentences.length < 3) {
            return issues;
        }
            
        const firstThird = sentences.slice(0, Math.floor(sentences.length / 3));
        
        const conclusionIndicators = [
            /\b(recommend|suggest|conclude|believe|think|decision)/gi,
            /\b(in summary|to summarize|bottom line|the point is)/gi,
            /\b(action item|next steps|what to do)/gi
        ];
        
        const hasEarlyConclusion = firstThird.some(sentence => 
            conclusionIndicators.some(pattern => pattern.test(sentence))
        );
        
        if (!hasEarlyConclusion) {
            issues.push("Main conclusion or recommendation may be buried - consider leading with the key takeaway");
        }
        
        return issues;
    }

    checkSentenceStructure(text) {
        const issues = [];
        const sentences = text.split('.').filter(s => s.trim());
        
        for (const sentence of sentences) {
            if (sentence.split(' ').length > 30) {
                issues.push(`Very long sentence (${sentence.split(' ').length} words): '${sentence.substring(0, 50)}...'`);
            }
            
            const weakOpenings = [
                /^there (is|are|was|were)\b/gi,
                /^it (is|was)\b.*that/gi,
                /^what (is|was)\b/gi,
                /^the fact that\b/gi
            ];
            
            for (const pattern of weakOpenings) {
                if (pattern.test(sentence)) {
                    issues.push(`Consider stronger sentence opening: '${sentence.substring(0, 50)}...'`);
                    break;
                }
            }
        }
        
        return issues;
    }

    checkActiveVoice(text) {
        const issues = [];
        
        const passivePatterns = [
            /\b(was|were|is|are|been|being)\s+\w+ed\b/gi,
            /\b(was|were|is|are)\s+\w+\s+by\s+\w+/gi
        ];
        
        const sentences = text.split('.');
        for (let sentence of sentences) {
            sentence = sentence.trim().toLowerCase();
            for (const pattern of passivePatterns) {
                if (pattern.test(sentence)) {
                    issues.push(`Passive voice detected: '${sentence.substring(0, 60)}...'`);
                    break;
                }
            }
        }
        
        return issues;
    }

    checkLogicalFlow(text) {
        const issues = [];
        
        const transitionIndicators = [
            /\b(first|second|third|next|then|furthermore|moreover|however|therefore|consequently)\b/gi
        ];
        
        const hasTransitions = transitionIndicators.some(pattern => pattern.test(text));
        const hasStructure = /\b(1\.|2\.|3\.|first|second|third|-|\*)\b/gi.test(text);
        
        const wordCount = text.split(' ').length;
        if (wordCount > 150) {
            if (!hasTransitions && !hasStructure) {
                issues.push("Long text lacks clear logical structure - consider adding transitions or organizing in numbered points");
            }
        }
        
        return issues;
    }

    checkConciseness(text) {
        const issues = [];
        
        const redundancies = [
            { pattern: /\babsolutely essential\b/gi, replacement: 'essential' },
            { pattern: /\bin order to\b/gi, replacement: 'to' },
            { pattern: /\bdue to the fact that\b/gi, replacement: 'because' },
            { pattern: /\bfor the purpose of\b/gi, replacement: 'to' }
        ];
        
        for (const { pattern, replacement } of redundancies) {
            if (pattern.test(text)) {
                issues.push(`Redundant phrase found - consider using '${replacement}' instead`);
            }
        }
        
        const fillerPatterns = [/\b(very|really|quite|rather|somewhat|quite a bit)\b/gi];
        const fillerCount = fillerPatterns.reduce((count, pattern) => {
            const matches = text.match(pattern);
            return count + (matches ? matches.length : 0);
        }, 0);
        
        const wordCount = text.split(' ').length;
        if (fillerCount > wordCount * 0.02) {
            issues.push(`Excessive use of filler words (${fillerCount} instances) - consider removing some`);
        }
        
        return issues;
    }

    checkClaritySimplicity(text) {
        const issues = [];
        
        const jargonPatterns = [
            /\b(utilize|utilization)\b/gi,
            /\b(facilitate|facilitation)\b/gi,
            /\b(leverage)\b(?=.*business)/gi,
            /\b(paradigm|synergistic|holistic)\b/gi,
            /\b(optimal|optimize|optimization)\b/gi
        ];
        
        for (const pattern of jargonPatterns) {
            if (pattern.test(text)) {
                issues.push("Jargon detected - consider simpler alternatives");
            }
        }
        
        return issues;
    }

    checkEliminateClutter(text) {
        const issues = [];
        
        const clutterWords = [
            /\b(very|really|quite|rather|somewhat|pretty|fairly|relatively)\b/gi,
            /\b(kind of|sort of|basically|essentially|literally|actually|totally)\b/gi
        ];
        
        let clutterCount = 0;
        for (const pattern of clutterWords) {
            const matches = text.match(pattern);
            clutterCount += matches ? matches.length : 0;
        }
        
        const wordCount = text.split(' ').length;
        if (clutterCount > wordCount * 0.03) {
            issues.push(`High clutter word density (${clutterCount} instances) - remove unnecessary qualifiers`);
        }
        
        return issues;
    }

    // Suggestion Methods
    suggestSuperSpecificHow() {
        return [
            "• Add specific steps, examples, or concrete implementation details",
            "• Replace vague advice with actionable instructions",
            "• Include time estimates, specific tools, or measurable outcomes"
        ];
    }

    suggestCutBackstory() {
        return [
            "• Consider starting closer to the main point or key insight",
            "• Ask: 'Does this opening sentence directly serve my reader's immediate need?'",
            "• Try starting with the insight or recommendation, then provide minimal necessary context"
        ];
    }

    suggestClearRecommendations() {
        return [
            "• State your recommendation upfront (e.g., 'I recommend X because...')",
            "• If presenting options, clearly indicate which you prefer and why",
            "• Replace hedging language with confident statements where appropriate"
        ];
    }

    suggestBottomLineFirst() {
        return [
            "• Start with: 'Bottom line: [your main point]'",
            "• Or begin with: 'I recommend [action] because [key reason]'",
            "• Move supporting details and context after the main point"
        ];
    }

    suggestSentenceStructure() {
        return [
            "• Break sentences longer than 25-30 words into shorter, clearer sentences",
            "• Start sentences with strong subjects and active verbs when possible",
            "• Avoid starting with 'There is/are' - use more direct constructions"
        ];
    }

    suggestActiveVoice() {
        return [
            "• Rewrite passive voice to active voice for stronger, clearer writing",
            "• Put the doer of the action before the verb when possible",
            "• Example: 'The report was written by John' → 'John wrote the report'"
        ];
    }

    suggestLogicalFlow() {
        return [
            "• Use transition words to guide readers through your argument",
            "• Start each paragraph with a clear topic sentence",
            "• Organize ideas in logical order: most important first, supporting details second"
        ];
    }

    suggestConciseness() {
        return [
            "• Remove redundant phrases and unnecessary words",
            "• Replace wordy constructions with shorter alternatives",
            "• Example: 'in order to' → 'to', 'due to the fact that' → 'because'"
        ];
    }

    suggestClaritySimplicity() {
        return [
            "• Replace jargon with simple, clear words",
            "• Use 'use' instead of 'utilize', 'help' instead of 'facilitate'",
            "• Break complex sentences into shorter, clearer ones"
        ];
    }

    suggestEliminateClutter() {
        return [
            "• Remove clutter words: 'very', 'really', 'quite', 'rather', 'somewhat'",
            "• Strengthen weak words instead of adding qualifiers",
            "• Example: 'very good' → 'excellent', 'really important' → 'crucial'"
        ];
    }
}

// Global variables and event handlers
const bot = new WritingBot();

function updateWordCount() {
    const text = document.getElementById('textInput').value;
    const wordCount = text.trim() ? text.trim().split(/\s+/).length : 0;
    document.getElementById('wordCount').textContent = `${wordCount} words`;
}

function analyzeText() {
    const text = document.getElementById('textInput').value.trim();
    
    if (!text) {
        alert('Please enter some text to analyze.');
        return;
    }

    const analyzeBtn = document.getElementById('analyzeBtn');
    const btnText = analyzeBtn.querySelector('.btn-text');
    const btnIcon = analyzeBtn.querySelector('.btn-icon');
    
    // Show loading state
    analyzeBtn.disabled = true;
    btnText.textContent = 'Analyzing...';
    btnIcon.innerHTML = '<div class="loading"></div>';

    // Simulate analysis delay for better UX
    setTimeout(() => {
        const results = bot.analyzeText(text);
        displayResults(results);
        
        // Reset button
        analyzeBtn.disabled = false;
        btnText.textContent = 'Analyze Text';
        btnIcon.textContent = '📊';
    }, 1000);
}

function displayResults(results) {
    const resultsSection = document.getElementById('results');
    const analysisContent = document.getElementById('analysisContent');
    
    let html = '';
    let allPassed = true;
    
    // Display analysis for each rule
    for (const [ruleName, ruleAnalysis] of Object.entries(results.analysis)) {
        const displayName = ruleName.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
        const status = ruleAnalysis.passed ? '✓ PASS' : '✗ ISSUES FOUND';
        const statusClass = ruleAnalysis.passed ? 'pass' : 'fail';
        const statusIcon = ruleAnalysis.passed ? '✅' : '❌';
        
        if (!ruleAnalysis.passed) {
            allPassed = false;
        }
        
        html += `
            <div class="result-item ${statusClass}">
                <div class="result-header">
                    <span class="status-indicator">${statusIcon}</span>
                    <span class="result-title">${displayName}: ${status}</span>
                </div>
                <div class="result-description">${ruleAnalysis.description}</div>
                ${ruleAnalysis.issues.length > 0 ? `
                    <ul class="issues-list">
                        ${ruleAnalysis.issues.map(issue => `<li>${issue}</li>`).join('')}
                    </ul>
                ` : ''}
            </div>
        `;
    }
    
    // Add suggestions if any issues were found
    if (results.suggestions.length > 0) {
        html += `
            <div class="suggestions">
                <h3>💡 Suggestions for Improvement</h3>
                <ul>
                    ${results.suggestions.map(suggestion => `<li>${suggestion}</li>`).join('')}
                </ul>
            </div>
        `;
    }
    
    analysisContent.innerHTML = html;
    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
    
    // Show completion message
    setTimeout(() => {
        if (allPassed) {
            alert('🎉 Great! Your text follows the writing principles well!');
        } else {
            alert('💡 Consider applying the suggestions above to improve your writing.');
        }
    }, 500);
}

function clearText() {
    document.getElementById('textInput').value = '';
    document.getElementById('results').style.display = 'none';
    document.getElementById('wordCount').textContent = '0 words';
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    const textInput = document.getElementById('textInput');
    
    textInput.addEventListener('input', updateWordCount);
    
    textInput.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            analyzeText();
        }
    });
    
    // Initial word count
    updateWordCount();
});
