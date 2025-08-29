from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from matches.models import Match
from teams.models import Team

class LeagueTableView(APIView):
    def get(self, request):
        # جدول للفرق
        table = {}

        # ابدأ كل فريق من صفر
        for team in Team.objects.all():
            table[team.id] = {
                "team": team.name,
                "played": 0,
                "wins": 0,
                "draws": 0,
                "losses": 0,
                "goals_scored": 0,
                "goals_conceded": 0,
                "points": 0
            }

        # عدل الجدول بناءً على الماتشات
        for match in Match.objects.all():
            home = table[match.home_team.id]
            away = table[match.away_team.id]

            # تحديث عدد المباريات
            home["played"] += 1
            away["played"] += 1

            # الأهداف
            home["goals_scored"] += match.home_score
            home["goals_conceded"] += match.away_score
            away["goals_scored"] += match.away_score
            away["goals_conceded"] += match.home_score

            # تحديد الفائز
            if match.home_score > match.away_score:
                home["wins"] += 1
                home["points"] += 3
                away["losses"] += 1
            elif match.home_score < match.away_score:
                away["wins"] += 1
                away["points"] += 3
                home["losses"] += 1
            else:
                home["draws"] += 1
                away["draws"] += 1
                home["points"] += 1
                away["points"] += 1

        # ترتيب الجدول (حسب النقاط والفرق)
        sorted_table = sorted(
            table.values(),
            key=lambda x: (x["points"], x["goals_scored"] - x["goals_conceded"]),
            reverse=True
        )

        return Response(sorted_table)
