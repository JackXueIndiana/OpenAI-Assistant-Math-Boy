# OpenAI-Assistant-Math-Boy
The learning material is from here:
~~~
https://learn.microsoft.com/en-us/azure/ai-services/openai/assistants-quickstart?tabs=command-line%2Ctypescript&pivots=programming-language-ai-studio
~~~
After you tried out in AI Studio, you can try the assistant in code. The generated code needs some clean-up and replacement.

When you run the code you should see
~~~
python testme.py
SyncCursorPage[Message](data=[Message(id='msg_sBhvjgR9GldoeyjKqoXxctnM', assistant_id='asst_XjvRxybM3ikTbs3ZLWJzkPnm', attachments=[], completed_at=None, content=[TextContentBlock(text=Text(annotations=[], value="Of course! I'd be happy to help you solve the equation 3x + 11 = 14. \n\nTo solve this equation, we need to isolate the variable x on one side of the equation. We can do this by performing the same operations on both sides of the equation to maintain equality.\n\nLet's start by subtracting 11 from both sides of the equation:\n\n3x + 11 - 11 = 14 - 11\n\nSimplifying the equation gives:\n\n3x = 3\n\nTo isolate x, we need to divide both sides of the equation by 3:\n\n(3x)/3 = 3/3\n\nSimplifying further:\n\nx = 1\n\nTherefore, the solution to the equation 3x + 11 = 14 is x = 1."), type='text')], created_at=1723045671, incomplete_at=None, incomplete_details=None, metadata={}, object='thread.message', role='assistant', run_id='run_x8fZUCnjaUBPYTqdl6rUBFwW', status=None, thread_id='thread_ADRae4PGBMEynyXpSpPx6ifV'), Message(id='msg_0rxnRDRR1dLDLmwO5biPDenP', assistant_id=None, attachments=[], completed_at=None, content=[TextContentBlock(text=Text(annotations=[], value='I need to solve the equation 3x + 11 = 14. Can you help me?'), type='text')], created_at=1723045661, incomplete_at=None, incomplete_details=None, metadata={}, object='thread.message', role='user', run_id=None, status=None, thread_id='thread_ADRae4PGBMEynyXpSpPx6ifV')], object='list', first_id='msg_sBhvjgR9GldoeyjKqoXxctnM', last_id='msg_0rxnRDRR1dLDLmwO5biPDenP', has_more=False)
~~~
