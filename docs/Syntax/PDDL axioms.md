

PDDL axioms

https://icaps16.icaps-conference.org/proceedings/summer-school/Rintanen.pdf

Computational Complexity in AutomatedPlanning and Scheduling

从计算理论的时间维度审视，PDDL并非图灵完备语言，其根本原因在于缺乏无限长度的纸带模型，因而无法实现通用计算能力。

[In defense of PDDL axioms](https://www.sciencedirect.com/science/article/pii/S0004370205000810

```
<domain>                ::= (define (domain <name>)
[<constant-def>]
[<predicates-def>]
[<axiom-def>*]
<action-def>*)

<constants-def>         ::= (:constants <name>+)
<predicate-def>         ::= (:predicates <skeleton>+)
<skeleton>              ::= (<predicate> <variable>*)
<predicate>             ::= <name>
<variable>              ::= ?<name>
<axiom-def>             ::= (:derived <skeleton> <formula>)
<formula>               ::= <atomic-formula>
<formula>               ::= (not <formula>)
<formula>               ::= (and <formula> <formula>+)
<formula>               ::= (or <formula> <formula>+)
<formula>               ::= (imply <formula> <formula>)
<formula>               ::= (exists (<variable>+) <formula>)
<formula>               ::= (forall (<variable>+) <formula>)
<atomic-formula>        ::= (<predicate> <term>*)
<ground-atomic-formula> ::= (<predicate> <name>*)
<term>                  ::= <name>
<term>                  ::= <variable>
<action-def>            ::= (:action <name>:parameters (<variable>*)<action-def body>)
<action-def body>       ::= [:precondition <formula>]:effect <eff-formula>
<eff-formula>           ::= <one-eff-formula>
<eff-formula>           ::= (and <one-eff-formula><one-eff-formula>+)
<one-eff-formula>       ::= <atomic-effs>
<one-eff-formula>       ::= (when <formula> <atomic-effs>)
<one-eff-formula>       ::= (forall (<variable>+) <atomic-effs>)
<one-eff-formula>       ::= (forall (<variable>+)(when <formula> <atomic-effs>))
<atomic-effs>           ::= <literal>
<atomic-effs>           ::= (and <literal> <literal>+)
<literal>               ::= <atomic-formula>
<literal>               ::= (not <atomic-formula>)
<task>                  ::= (define (task <name>)(:domain <name>)<object declaration><init><goal>)
<object declaration>    ::= (:objects <name>*)
<init>                  ::= (:init <ground-atomic-formula>*)
<goal>                  ::= (:goal <formula>)
```







