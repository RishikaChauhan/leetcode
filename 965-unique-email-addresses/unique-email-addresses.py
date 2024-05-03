class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for email in emails:
            local, domain = email.split("@")
            # if '+' in local:
            local = local.split('+')[0].replace(".","")
            res.append(local+'@'+domain)
        return len(set(res))
        
        
        
        
        
        
        
        
        
        # res = []
        # for email in emails:
        #     i = email.index('@')
        #     if '+' in email:
        #         new = ''
        #         for char in email:
        #             if char == '+':
        #                 break
        #             elif char != '.':
        #                 new +=char
                
        #         res.append(new+email[i:])
        #     else:
        #         first = email[:i]
        #         new = ''
        #         for char in first:
        #             if char!='.':
        #                 new+=char
        #             new_email = new+email[i:]
        #         res.append(new_email)
        # return len(set(res))