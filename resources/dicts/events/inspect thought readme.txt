inspect thought nodes
id: the id that points to this node
text: the text that can randomly generate at the node
to: next possible node - if is null, it is a conclusion / leaf.
from: previous nodes - if is null, it is an intro / root
tags: defines what conditions must be met to enter a node 
	
	need at least a default path for each option (root, stem, leaf) to have full scenario coverage
do we want roots , stems, leaves, seperate from each other? I don't think they should overlap. stems may have different pathways through to a conclusion, but eventually there should be one. keeping them separate I think would be best. maybe making sure each stem has at least 1 leaf/conclusion

*tips* if you need to draw out the relation (2) -> ("nightmare") -> ("wake_up"), do so to make sure there are no loops


{
	"id": "2",
	"text": ["m_c appears to r_c in a dream. r_c can't quite make out who this cat is, but it feels like {PRONOUN/r_c/subj} might know {PRONOUN/m_c/obj}."],
	"to": ["nightmare"],
	"from": [],
	"tags": []
},
{
	"id": "nightmare",
	"text": ["A chill goes down r_c's spine when they ask the other cat for their name, but there is no response. Just a set of wide eyes looking back at them. m_c tilts their head slowly and r_c feels their heart pound in their chest."],
	"to": ["wake_up_nightmare", "nightmare_continued"],
	"from": ["2"],
	"tags": []
},
{
	"id": "wake_up_nightmare",
	"text": ["r_c wakes with a start, still feeling their heartbeat quickening as though the danger hasn't left. They try not to think about what they saw. Later, although they can't stop thinking about it, something in their gut makes them nervous to mention it to anyone. They only smile and say they didn't sleep well."],
	"to": [],
	"from": ["nightmare"],
	"tags": []
}