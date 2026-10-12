from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = defaultdict(list)
        email_to_name ={}
        # Build the graph and map each email to its name
        for account in accounts:
            name= account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                # Connect every email to the first email
                graph[first_email].append(email)
                graph[email].append(first_email)
        visited = set()
        def dfs(email, emails):
            visited.add(email)
            emails.append(email)
            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, emails)
        res = []
        # Find each connected component
        for email in email_to_name:
            if email not in visited:
                emails = []
                dfs(email, emails)
                # Add name followed by sorted emails
                res.append([email_to_name[email]] + sorted(emails))
        return res