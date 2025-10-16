#!/usr/bin/env python3
"""
Briefly - Writing analysis tool based on Wes Kao's writing principles and classic writing guides.

This tool applies key writing rules from:
- Wes Kao's principles from Lenny's Podcast
- "It Was the Best of Sentences, It Was the Worst of Sentences" by June Casagrande
- "The Minto Pyramid Principle" by Barbara Minto
- "HBR Guide to Better Business Writing"
- "On Writing Well" by William Zinsser

Core principles:
1. Super Specific "How" - Focus on actionable implementation
2. Start Right Before You Get Eaten by the Bear - Cut backstory, get to the point
3. Content Hierarchy of BS - Use appropriate rigor for content length
4. Eyes Light Up Principle - Focus on genuinely engaging content
5. Avoid Communication Surprises - Be clear about recommendations
6. Bottom Line Up Front - Lead with conclusions, then context (Minto Pyramid)
7. Over-communicate - Provide adequate context
8. Sentence Structure - Use clear, concise sentences (Casagrande)
9. Logical Flow - Structure arguments logically (Minto Pyramid)
10. Active Voice - Prefer active over passive voice (Business Writing)
11. Clarity & Simplicity - Write clearly and simply (Zinsser)
12. Eliminate Clutter - Remove unnecessary words and complexity (Zinsser)
"""

import re
import argparse
from typing import List, Dict, Tuple


class Briefly:
    def __init__(self):
        self.rules = {
            "super_specific_how": {
                "description": "Focus on actionable 'how' rather than 'what' and 'why'",
                "check": self._check_super_specific_how,
                "suggest": self._suggest_super_specific_how
            },
            "cut_backstory": {
                "description": "Start right before you get eaten by the bear - cut unnecessary backstory",
                "check": self._check_backstory,
                "suggest": self._suggest_cut_backstory
            },
            "clear_recommendations": {
                "description": "Avoid communication surprises - be clear about your point of view",
                "check": self._check_clear_recommendations,
                "suggest": self._suggest_clear_recommendations
            },
            "bottom_line_first": {
                "description": "Lead with conclusions, then provide context (Minto Pyramid Principle)",
                "check": self._check_bottom_line_first,
                "suggest": self._suggest_bottom_line_first
            },
            "adequate_context": {
                "description": "Over-communicate - ensure sufficient context without overwhelming",
                "check": self._check_adequate_context,
                "suggest": self._suggest_adequate_context
            },
            "sentence_structure": {
                "description": "Use clear, concise sentences with proper structure (Casagrande principles)",
                "check": self._check_sentence_structure,
                "suggest": self._suggest_sentence_structure
            },
            "active_voice": {
                "description": "Prefer active voice over passive voice for clarity and directness",
                "check": self._check_active_voice,
                "suggest": self._suggest_active_voice
            },
            "logical_flow": {
                "description": "Structure arguments logically with clear hierarchy (Minto Pyramid)",
                "check": self._check_logical_flow,
                "suggest": self._suggest_logical_flow
            },
            "conciseness": {
                "description": "Eliminate unnecessary words and redundant phrases",
                "check": self._check_conciseness,
                "suggest": self._suggest_conciseness
            },
            "clarity_simplicity": {
                "description": "Write clearly and simply - avoid jargon and complex constructions (Zinsser)",
                "check": self._check_clarity_simplicity,
                "suggest": self._suggest_clarity_simplicity
            },
            "eliminate_clutter": {
                "description": "Remove unnecessary words, adverbs, and complexity (Zinsser principles)",
                "check": self._check_eliminate_clutter,
                "suggest": self._suggest_eliminate_clutter
            }
        }

    def analyze_text(self, text: str) -> Dict:
        """Analyze text against all writing rules and provide suggestions."""
        results = {
            "original_text": text,
            "analysis": {},
            "suggestions": [],
            "improved_text": text
        }
        
        for rule_name, rule in self.rules.items():
            issues = rule["check"](text)
            results["analysis"][rule_name] = {
                "passed": len(issues) == 0,
                "issues": issues,
                "description": rule["description"]
            }
            
            if issues:
                suggestions = rule["suggest"](text, issues)
                results["suggestions"].extend(suggestions)
        
        return results

    def _check_super_specific_how(self, text: str) -> List[str]:
        """Check if text focuses on specific implementation rather than just concepts."""
        issues = []
        
        # Look for vague advice without specific steps
        vague_patterns = [
            r'\b(you should|it\'s important to|make sure to)\s+(be|have|do|get|use)\s+\w+',
            r'\b(focus on|prioritize|emphasize)\s+\w+\s+(more|better)',
            r'\b(improve|enhance|optimize)\s+\w+\s+(in order to|to)\s+\w+'
        ]
        
        for pattern in vague_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                issues.append(f"Potential vague advice without specific implementation: '{matches[0]}'")

        # Check for specific implementation indicators
        specific_indicators = [
            r'\b(here\'s how|this is how|step 1|first,|second,|then|next)',
            r'\b(specifically|exactly|precisely)',
            r'\b(example|instance|case study)',
            r'\d+\s+(minutes|hours|days|steps)'
        ]
        
        has_specific_content = any(re.search(pattern, text, re.IGNORECASE) for pattern in specific_indicators)
        
        if not has_specific_content and len(text.split()) > 100:
            issues.append("Text lacks specific implementation details - consider adding 'how-to' elements")
        
        return issues

    def _suggest_super_specific_how(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Add specific steps, examples, or concrete implementation details")
        suggestions.append("• Replace vague advice with actionable instructions (e.g., 'Here's how to...' instead of 'You should...')")
        suggestions.append("• Include time estimates, specific tools, or measurable outcomes")
        return suggestions

    def _check_backstory(self, text: str) -> List[str]:
        """Check for excessive backstory that could be cut."""
        issues = []
        sentences = text.split('.')
        
        # Look for potential backstory indicators in first few sentences
        backstory_indicators = [
            r'\b(let me|i want to|first, let me|to begin with|in order to understand)',
            r'\b(context|background|history|overview|introduction)',
            r'\b(going to|about to|planning to|will be talking about)'
        ]
        
        first_third = sentences[:len(sentences)//3] if len(sentences) > 3 else sentences
        
        for sentence in first_third:
            for pattern in backstory_indicators:
                if re.search(pattern, sentence, re.IGNORECASE):
                    issues.append(f"Potential backstory in opening: '{sentence.strip()}'")
                    break
        
        return issues

    def _suggest_cut_backstory(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Consider starting closer to the main point or key insight")
        suggestions.append("• Ask: 'Does this opening sentence directly serve my reader's immediate need?'")
        suggestions.append("• Try starting with the insight or recommendation, then provide minimal necessary context")
        return suggestions

    def _check_clear_recommendations(self, text: str) -> List[str]:
        """Check if recommendations are clear and unambiguous."""
        issues = []
        
        # Look for unclear recommendations
        unclear_patterns = [
            r'\b(you might want to|it could be|perhaps|maybe|consider)',
            r'\b(on one hand|on the other hand)\b.*\b(on the other hand|however|but)\b',
            r'\b(pros and cons|advantages and disadvantages)\b(?!.*recommend)',
        ]
        
        for pattern in unclear_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                issues.append("Potentially unclear recommendation - consider stating your position more directly")
        
        # Check for hidden bias in neutral-sounding sections
        if re.search(r'\b(pros?|advantages?)\b.*\b(cons?|disadvantages?)\b', text, re.IGNORECASE):
            if not re.search(r'\b(recommend|suggest|think|believe)\b', text, re.IGNORECASE):
                issues.append("Pros/cons list detected without clear recommendation - state your position upfront")
        
        return issues

    def _suggest_clear_recommendations(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• State your recommendation upfront (e.g., 'I recommend X because...')")
        suggestions.append("• If presenting options, clearly indicate which you prefer and why")
        suggestions.append("• Replace hedging language with confident statements where appropriate")
        return suggestions

    def _check_bottom_line_first(self, text: str) -> List[str]:
        """Check if the main point comes early in the text."""
        issues = []
        sentences = text.split('.')
        
        if len(sentences) < 3:
            return issues
            
        first_third = sentences[:len(sentences)//3]
        
        # Look for conclusion indicators
        conclusion_indicators = [
            r'\b(recommend|suggest|conclude|believe|think|decision)',
            r'\b(in summary|to summarize|bottom line|the point is)',
            r'\b(action item|next steps|what to do)'
        ]
        
        has_early_conclusion = any(
            re.search(pattern, sentence, re.IGNORECASE) 
            for sentence in first_third 
            for pattern in conclusion_indicators
        )
        
        if not has_early_conclusion:
            issues.append("Main conclusion or recommendation may be buried - consider leading with the key takeaway")
        
        return issues

    def _suggest_bottom_line_first(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Start with: 'Bottom line: [your main point]'")
        suggestions.append("• Or begin with: 'I recommend [action] because [key reason]'")
        suggestions.append("• Move supporting details and context after the main point")
        return suggestions

    def _check_adequate_context(self, text: str) -> List[str]:
        """Check if text provides adequate context without being overwhelming."""
        issues = []
        word_count = len(text.split())
        
        # Check for insufficient context
        if word_count > 200:
            context_indicators = [
                r'\b(because|since|given that|considering|due to)',
                r'\b(context|background|premise|assumption)',
                r'\b(for example|for instance|such as)'
            ]
            
            has_context = any(re.search(pattern, text, re.IGNORECASE) for pattern in context_indicators)
            
            if not has_context and word_count > 300:
                issues.append("Long text may lack sufficient context or examples for reader comprehension")
        
        return issues

    def _suggest_adequate_context(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Add context if readers might need more background to understand")
        suggestions.append("• Use examples, analogies, or case studies to illustrate key points")
        suggestions.append("• Consider adding 'Context:' or 'Background:' sections for complex topics")
        return suggestions

    def _check_sentence_structure(self, text: str) -> List[str]:
        """Check for clear, well-structured sentences (based on Casagrande principles)."""
        issues = []
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        for sentence in sentences:
            # Check for overly long sentences
            if len(sentence.split()) > 30:
                issues.append(f"Very long sentence ({len(sentence.split())} words): '{sentence[:50]}...'")
            
            # Check for weak sentence openings
            weak_openings = [
                r'^there (is|are|was|were)\b',
                r'^it (is|was)\b.*that',
                r'^what (is|was)\b',
                r'^the fact that\b'
            ]
            
            for pattern in weak_openings:
                if re.match(pattern, sentence, re.IGNORECASE):
                    issues.append(f"Consider stronger sentence opening: '{sentence[:50]}...'")
                    break
            
            # Check for unclear pronoun references
            if re.search(r'\b(it|this|that|these|those)\b.*\b(it|this|that|these|those)\b', sentence, re.IGNORECASE):
                if len(re.findall(r'\b(it|this|that|these|those)\b', sentence, re.IGNORECASE)) > 2:
                    issues.append(f"Multiple unclear pronoun references: '{sentence[:50]}...'")
        
        return issues

    def _suggest_sentence_structure(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Break sentences longer than 25-30 words into shorter, clearer sentences")
        suggestions.append("• Start sentences with strong subjects and active verbs when possible")
        suggestions.append("• Avoid starting with 'There is/are' - use more direct constructions")
        suggestions.append("• Make pronoun references clear and specific")
        return suggestions

    def _check_active_voice(self, text: str) -> List[str]:
        """Check for passive voice usage that weakens writing."""
        issues = []
        
        # Common passive voice patterns
        passive_patterns = [
            r'\b(was|were|is|are|been|being)\s+\w+ed\b',
            r'\b(was|were|is|are)\s+\w+\s+by\s+\w+',
            r'\b(it was|they were|there was|there were)\s+\w+ed\b'
        ]
        
        sentences = text.split('.')
        for sentence in sentences:
            sentence = sentence.strip().lower()
            for pattern in passive_patterns:
                if re.search(pattern, sentence):
                    issues.append(f"Passive voice detected: '{sentence[:60]}...'")
                    break
        
        return issues

    def _suggest_active_voice(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Rewrite passive voice to active voice for stronger, clearer writing")
        suggestions.append("• Put the doer of the action before the verb when possible")
        suggestions.append("• Example: 'The report was written by John' → 'John wrote the report'")
        return suggestions

    def _check_logical_flow(self, text: str) -> List[str]:
        """Check for logical structure and flow (Minto Pyramid principles)."""
        issues = []
        
        # Check for transition words that indicate logical flow
        transition_indicators = [
            r'\b(first|second|third|next|then|furthermore|moreover|however|therefore|consequently)\b'
        ]
        
        has_transitions = any(re.search(pattern, text, re.IGNORECASE) for pattern in transition_indicators)
        
        # Check for numbered or bulleted lists
        has_structure = bool(re.search(r'\b(1\.|2\.|3\.|first|second|third|-|\*)\b', text, re.IGNORECASE))
        
        # For longer texts, check if there's clear structure
        word_count = len(text.split())
        if word_count > 150:
            if not (has_transitions or has_structure):
                issues.append("Long text lacks clear logical structure - consider adding transitions or organizing in numbered points")
        
        # Check for topic sentences at paragraph starts
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        for i, paragraph in enumerate(paragraphs):
            sentences = [s.strip() for s in paragraph.split('.') if s.strip()]
            if len(sentences) > 1:
                first_sentence = sentences[0]
                # Look for topic sentence indicators
                topic_indicators = [
                    r'\b(in this|we will|the main|this (section|chapter|part)|to summarize|in conclusion)\b',
                    r'\b(first|next|then|finally|overall|in summary)\b'
                ]
                
                has_topic_sentence = any(re.search(pattern, first_sentence, re.IGNORECASE) for pattern in topic_indicators)
                
                if not has_topic_sentence and len(first_sentence.split()) > 15:
                    issues.append(f"Paragraph {i+1} may lack a clear topic sentence")
                    break
        
        return issues

    def _suggest_logical_flow(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Use transition words to guide readers through your argument")
        suggestions.append("• Start each paragraph with a clear topic sentence")
        suggestions.append("• Organize ideas in logical order: most important first, supporting details second")
        suggestions.append("• Consider using numbered lists or bullet points for clarity")
        return suggestions

    def _check_conciseness(self, text: str) -> List[str]:
        """Check for unnecessary words and redundancy."""
        issues = []
        
        # Common redundant phrases
        redundancies = [
            (r'\babsolutely essential\b', 'essential'),
            (r'\bcompletely finished\b', 'finished'),
            (r'\bfirst and foremost\b', 'first'),
            (r'\bif and when\b', 'when'),
            (r'\bin order to\b', 'to'),
            (r'\bin the event that\b', 'if'),
            (r'\bdue to the fact that\b', 'because'),
            (r'\bfor the purpose of\b', 'to'),
            (r'\bprevious experience\b', 'experience'),
            (r'\badvance planning\b', 'planning'),
            (r'\bclose proximity\b', 'near')
        ]
        
        for pattern, replacement in redundancies:
            if re.search(pattern, text, re.IGNORECASE):
                issues.append(f"Redundant phrase found - consider using '{replacement}' instead")
        
        # Check for excessive use of filler words
        filler_patterns = [
            r'\b(very|really|quite|rather|somewhat|quite a bit)\b'
        ]
        
        filler_count = sum(len(re.findall(pattern, text, re.IGNORECASE)) for pattern in filler_patterns)
        word_count = len(text.split())
        
        if filler_count > word_count * 0.02:  # More than 2% filler words
            issues.append(f"Excessive use of filler words ({filler_count} instances) - consider removing some")
        
        return issues

    def _suggest_conciseness(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Remove redundant phrases and unnecessary words")
        suggestions.append("• Replace wordy constructions with shorter alternatives")
        suggestions.append("• Avoid filler words like 'very', 'really', 'quite' when possible")
        suggestions.append("• Example: 'in order to' → 'to', 'due to the fact that' → 'because'")
        return suggestions

    def _check_clarity_simplicity(self, text: str) -> List[str]:
        """Check for clarity and simplicity (Zinsser principles)."""
        issues = []
        
        # Check for jargon and complex constructions
        jargon_patterns = [
            r'\b(utilize|utilization)\b',  # Should be "use"
            r'\b(facilitate|facilitation)\b',  # Often means "help"
            r'\b(leverage)\b(?=.*business)',  # Overused business jargon
            r'\b(paradigm|synergistic|holistic)\b',  # Pretentious words
            r'\b(optimal|optimize|optimization)\b',
            r'\b(innovative solution|best practices|mission-critical)\b'
        ]
        
        for pattern in jargon_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                issues.append(f"Jargon detected - consider simpler alternatives: '{matches[0]}'")
        
        # Check for unnecessarily complex sentence structures
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        for sentence in sentences:
            # Check for multiple clauses that could be simplified
            clause_count = len(re.findall(r'\b(and|but|however|although|while|whereas)\b', sentence))
            if clause_count > 2 and len(sentence.split()) > 25:
                issues.append(f"Complex sentence structure - consider breaking into simpler sentences")
                break
        
        # Check for overly formal language that could be more direct
        formal_phrases = [
            (r'\bin order to\b', 'to'),
            (r'\bwith regard to\b', 'about'),
            (r'\bin the event that\b', 'if'),
            (r'\bfor the purpose of\b', 'to'),
            (r'\bid est\b', 'that is'),
            (r'\bvis-à-vis\b', 'compared to')
        ]
        
        for pattern, replacement in formal_phrases:
            if re.search(pattern, text, re.IGNORECASE):
                issues.append(f"Formal phrase could be simplified: consider using '{replacement}'")
        
        return issues

    def _suggest_clarity_simplicity(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Replace jargon with simple, clear words")
        suggestions.append("• Use 'use' instead of 'utilize', 'help' instead of 'facilitate'")
        suggestions.append("• Break complex sentences into shorter, clearer ones")
        suggestions.append("• Avoid unnecessarily formal language - write as you speak")
        suggestions.append("• Example: 'utilize' → 'use', 'facilitate' → 'help', 'leverage' → 'use'")
        return suggestions

    def _check_eliminate_clutter(self, text: str) -> List[str]:
        """Check for clutter words and unnecessary complexity (Zinsser)."""
        issues = []
        
        # Zinsser's classic clutter words
        clutter_words = [
            r'\b(very|really|quite|rather|somewhat|pretty|fairly|relatively)\b',
            r'\b(in a very real sense|it is important to note that|needless to say)\b',
            r'\b(kind of|sort of|basically|essentially|literally|actually|totally)\b'
        ]
        
        clutter_count = 0
        for pattern in clutter_words:
            matches = re.findall(pattern, text, re.IGNORECASE)
            clutter_count += len(matches)
        
        word_count = len(text.split())
        if clutter_count > word_count * 0.03:  # More than 3% clutter words
            issues.append(f"High clutter word density ({clutter_count} instances) - remove unnecessary qualifiers")
        
        # Check for unnecessary adverbs that weaken verbs
        weak_adverbs = [
            r'\b(slightly|somewhat|fairly|rather|quite) (good|bad|nice|important|interesting)\b',
            r'\b(very|really|extremely) \w+ly\b',  # Very clearly, really quickly
            r'\btotally\s+(different|wrong|correct|right)\b'
        ]
        
        for pattern in weak_adverbs:
            if re.search(pattern, text, re.IGNORECASE):
                issues.append("Weak adverb + adjective combination detected - strengthen the word itself")
                break
        
        # Check for redundant phrases that add no meaning
        redundant_phrases = [
            r'\badvance warning\b',  # warnings are always in advance
            r'\btrue facts\b',  # facts are always true
            r'\bgather together\b',  # gathering implies togetherness
            r'\bplan ahead\b',  # planning implies ahead
            r'\bfree gift\b',  # gifts are always free
            r'\bnew innovation\b'  # innovations are always new
        ]
        
        for pattern in redundant_phrases:
            if re.search(pattern, text, re.IGNORECASE):
                issues.append(f"Redundant phrase detected - remove unnecessary word")
                break
        
        return issues

    def _suggest_eliminate_clutter(self, text: str, issues: List[str]) -> List[str]:
        suggestions = []
        suggestions.append("• Remove clutter words: 'very', 'really', 'quite', 'rather', 'somewhat'")
        suggestions.append("• Strengthen weak words instead of adding qualifiers")
        suggestions.append("• Eliminate redundant phrases like 'advance warning' or 'new innovation'")
        suggestions.append("• Example: 'very good' → 'excellent', 'really important' → 'crucial'")
        suggestions.append("• Zinsser's rule: Every word must earn its place")
        return suggestions

    def generate_improved_text(self, analysis: Dict) -> str:
        """Generate improved version of text based on analysis."""
        text = analysis["original_text"]
        
        # Apply suggestions based on issues found
        for rule_name, rule_analysis in analysis["analysis"].items():
            if not rule_analysis["passed"] and rule_analysis["issues"]:
                if rule_name == "bottom_line_first":
                    text = self._apply_bottom_line_first(text)
                elif rule_name == "clear_recommendations":
                    text = self._apply_clear_recommendations(text)
                # Add more transformations as needed
        
        return text

    def _apply_bottom_line_first(self, text: str) -> str:
        """Attempt to restructure text to put bottom line first."""
        # This is a simplified implementation
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        if len(sentences) > 2:
            # Look for a conclusion sentence and move it earlier
            conclusion_patterns = [
                r'\b(recommend|suggest|conclude|believe|think)',
                r'\b(summary|bottom line|point is)'
            ]
            
            for i, sentence in enumerate(sentences):
                if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in conclusion_patterns):
                    if i > 1:  # If conclusion is not in first few sentences
                        # Move conclusion to front
                        conclusion = sentences.pop(i)
                        sentences.insert(1, conclusion)
                        break
        
        return '. '.join(sentences) + ('.' if text.endswith('.') else '')

    def _apply_clear_recommendations(self, text: str) -> str:
        """Attempt to make recommendations clearer."""
        # Add clear recommendation language if missing
        if not re.search(r'\b(recommend|suggest|believe|think we should)\b', text, re.IGNORECASE):
            if re.search(r'\b(pros?|advantages?)\b.*\b(cons?|disadvantages?)\b', text, re.IGNORECASE):
                text = "Recommendation: " + text
        
        return text


def main():
    parser = argparse.ArgumentParser(description="Writing Bot - Improve your writing based on Wes Kao's principles")
    parser.add_argument("text", nargs="?", help="Text to analyze (or read from stdin)")
    parser.add_argument("--file", "-f", help="Read text from file")
    parser.add_argument("--output", "-o", help="Output file for results")
    
    args = parser.parse_args()
    
    bot = Briefly()
    
    # Get input text
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("Enter text to analyze (press Ctrl+D when done):")
        text = ""
        try:
            while True:
                line = input()
                text += line + "\n"
        except EOFError:
            pass
    
    if not text.strip():
        print("No text provided")
        return
    
    # Analyze text
    analysis = bot.analyze_text(text)
    
    # Display results
    print("\n" + "="*60)
    print("WRITING ANALYSIS - ENHANCED WITH CLASSIC WRITING GUIDES")
    print("="*60)
    print("Based on: Wes Kao's principles + Casagrande + Minto Pyramid + HBR Guide + Zinsser")
    
    print(f"\nOriginal text ({len(text.split())} words):")
    print("-" * 40)
    print(text[:200] + "..." if len(text) > 200 else text)
    
    print(f"\nANALYSIS RESULTS:")
    print("-" * 40)
    
    all_passed = True
    for rule_name, rule_analysis in analysis["analysis"].items():
        status = "✓ PASS" if rule_analysis["passed"] else "✗ ISSUES FOUND"
        print(f"\n{rule_name.replace('_', ' ').title()}: {status}")
        print(f"  {rule_analysis['description']}")
        
        if not rule_analysis["passed"]:
            all_passed = False
            print("  Issues:")
            for issue in rule_analysis["issues"]:
                print(f"    • {issue}")
    
    if analysis["suggestions"]:
        print(f"\nSUGGESTIONS FOR IMPROVEMENT:")
        print("-" * 40)
        for suggestion in analysis["suggestions"]:
            print(f"  {suggestion}")
    
    if all_passed:
        print(f"\n🎉 Great! Your text follows Wes Kao's writing principles well!")
    else:
        print(f"\n💡 Consider applying the suggestions above to improve your writing.")
    
    # Output to file if requested
    if args.output:
        with open(args.output, 'w') as f:
            f.write(f"Writing Analysis Results\n")
            f.write(f"======================\n\n")
            f.write(f"Original text:\n{text}\n\n")
            f.write(f"Analysis:\n{analysis}\n")
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
